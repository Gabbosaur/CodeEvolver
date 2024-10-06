import os
import ollama  # Ensure the Ollama module is installed and running locally
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
import re


load_dotenv()

LLM_MODE = os.getenv('LLM_MODE')


client = None
if LLM_MODE == 'GROQ':
    print(os.getenv("GROQ_API_KEY"))
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Hardcoded folder path and target language
FOLDER_PATH = './legacy_project/'  # <-- Set your folder path here
TARGET_PATH = './translated/'
TARGET_LANGUAGE = 'Java'  # Default target language for translation is set to Java

# Function to get files based on extensions
def get_source_files(folder_path, extensions):
    source_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extensions):
                source_files.append(os.path.join(root, file))
    return source_files

# Function to interact with the local Ollama model for code translation
def translate_code_with_ollama(source_code, source_language, target_language='Java'):
    # Define the prompt for code translation
    prompt = f"Translate the following {source_language} code to {target_language}:\n\n{source_code}"

    # Call Ollama and pass the prompt
    result = ollama.chat(model='codellama', messages=[
        {
            'role': 'user',
            'content': prompt,
        }
    ])

    # Extract the translated code from the output
    translated_code = result['message'].strip()  # Access 'message' field from Ollama's response
    return translated_code

def extract_java_code(text):
    start = text.find("```java") + len("```java")
    end = text.find("```", start)

    if start != -1 and end != -1:
        # Extract the Java code and remove leading/trailing whitespaces
        java_code_extracted = text[start:end].strip()
        return java_code_extracted
    else:
        print("No valid Java code block found in the text.")
        return None

def translate_code_with_groq(source_code, source_language, target_language='Java'):
    prompt = f"Translate the following {source_language} code to {target_language}, please generate only one java code block and don't propose multiple solutions:\n\n{source_code}"
    # Call Groq's API with the given prompt
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You're an expert Java developer."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",  # Ensure you use the appropriate Groq model
            temperature=0
        )

        # Extract the response content
        response_text = chat_completion.choices[0].message.content.strip()

        # Extract the Java code using the find() method
        improved_code = extract_java_code(response_text)
    
        print(improved_code)
        return improved_code, response_text  # Return both the code and the full response

    except Exception as e:
        print(f"Error during code translation: {e}")
        return None, None

# Function to determine the language of the source file based on its extension
def detect_language(file_path):
    if file_path.endswith('.py'):
        return 'Python'
    elif file_path.endswith('.cob') or file_path.endswith('.cbl'):
        return 'COBOL'
    elif file_path.endswith('.java'):
        return 'Java'
    else:
        return None
    
def replace_class_name(java_code: str, new_class_name: str) -> str:
    # Use a regex pattern to find the class name
    pattern = r'\bclass\s+(\w+)\b'
    match = re.search(pattern, java_code)
    
    if match:
        old_class_name = match.group(1)  # Get the old class name
        # Replace the old class name with the new class name
        updated_code = java_code.replace(old_class_name, new_class_name)
        return updated_code
    else:
        # raise ValueError("No class name found in the provided Java code.")
        return java_code

# Function to write the translated code to a file
def write_transformed_code(output_folder, file_path, transformed_code):
    os.makedirs(output_folder, exist_ok=True)
    file_name = Path(file_path).stem + ".java"
    output_path = os.path.join(output_folder, file_name.capitalize())
    
    transformed_code = replace_class_name(transformed_code, file_name.split('.')[0].capitalize())
    print("transformed_code:\n" + transformed_code)
    with open(output_path, 'w') as f:
        f.write(transformed_code)
    
    print(f"Translated code written to {output_path}")

# Main function to process the folder, translate, and save the output
def main(folder_path=FOLDER_PATH, target_language=TARGET_LANGUAGE):
    # Get all files that need to be processed (Python, COBOL, Java)
    source_files = get_source_files(folder_path, ('.py', '.cob', '.cbl', '.java'))

    # Output folder for transformed/translated files
    output_folder = os.path.join(TARGET_PATH)

    for file_path in source_files:
        print(f"Processing {file_path}")
        
        # Detect the language of the file
        source_language = detect_language(file_path)
        if source_language is None:
            print(f"Skipping unsupported file: {file_path}")
            continue

        # Read the source code
        with open(file_path, 'r') as f:
            source_code = f.read()

        if LLM_MODE == 'GROQ':
            # Translate the code using Groq 
            translated_code, response_text = translate_code_with_groq(source_code, source_language, target_language)
        else:
            # TODO ollama should have the same behavior as groq
            # Translate the code using Ollama
            translated_code = translate_code_with_ollama(source_code, source_language, target_language)
        
        # Write the transformed code to the output folder
        write_transformed_code(output_folder, file_path, translated_code)

# Run the main function with the hardcoded folder path and target language
if __name__ == '__main__':
    main(FOLDER_PATH, TARGET_LANGUAGE)
