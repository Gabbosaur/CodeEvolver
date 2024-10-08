import os
import ollama  # Ensure the Ollama module is installed and running locally
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
import re
import shutil

load_dotenv()

LLM_MODE = os.getenv('LLM_MODE')


client = None
if LLM_MODE == 'GROQ':
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


def extract_java_code(text):
    start = text.find("```java") + len("```java")
    end = text.find("```", start)

    if start != -1 and end != -1:
        # Extract the Java code and remove leading/trailing whitespaces
        java_code_extracted = text[start:end].strip()
        # java_test_extracted = new_text[start_test:end_test].strip()
        return java_code_extracted#, java_test_extracted
    else:
        print("No valid Java code block found in the text.")
        return None

# Function to interact with the local Ollama model for code translation
def ask_to_ollama(prompt):
    # Call Ollama and pass the prompt
    result = ollama.chat(model='codellama', messages=[
        {
            'role': 'user',
            'content': prompt,
        }
    ])

    # Extract the translated code from the output
    response_text = result['message'].strip()  # Access 'message' field from Ollama's response
    translated_code = extract_java_code(response_text)
    return translated_code, response_text

def ask_to_groq(system_prompt, prompt):
    # Call Groq's API with the given prompt
    try:
        chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                #model="llama-3.1-8b-instant",  # Ensure you use the appropriate Groq model
                # model="llama3-8b-8192",
                model="llama-3.1-70b-versatile",
                #model="mixtral-8x7b-32768",
                temperature=0
            )
        # Extract the response content
        response_text = chat_completion.choices[0].message.content.strip()
        print(response_text)

        translated_code = extract_java_code(response_text)
        return translated_code, response_text  # Return both the code and the full response
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
    
# Function to write the translated code to a file
def write_translated_code(output_folder, transformed_code, response_text):
    os.makedirs(output_folder, exist_ok=True)
    file_name = get_class_names(transformed_code)[0] + ".java"
    output_path = os.path.join(output_folder, file_name)        
    
    with open(output_path, 'w') as f:
        f.write(transformed_code)

    print(f"Translated code written to {output_path}")


def translate_code(source_code, source_language, target_language):
    system_prompt = f"I want you to act as a code translator. I will provide you with code in a specific source language, and I want you to translate it into a different target language. The translation should maintain the same functionalities as the original code, but using an object-oriented approach. Additionally, you should include plenty of comments to enhance readability. After that remember to add public methods for future unit testing.\n\n"
    prompt = f"Translate the following from {source_language} to {target_language}:\n\n{source_code}"

    if LLM_MODE == 'GROQ':
        # Translate the code using Groq 
        return ask_to_groq(system_prompt, prompt)
    else:
        # Translate the code using Ollama
        return ask_to_ollama(system_prompt + prompt)

def remove_comments(java_code):
    # Remove single-line comments (//...)
    java_code = re.sub(r'//.*', '', java_code)
    
    # Remove multi-line comments (/* ... */)
    java_code = re.sub(r'/\*.*?\*/', '', java_code, flags=re.DOTALL)
    
    return java_code

def get_class_names(java_code):
    # First, remove all comments from the code
    java_code_no_comments = remove_comments(java_code)

    # Regular expression to match class names (public, private, and static classes or interfaces)
    class_pattern = r'\b(class|interface)\s+(\w+)'
    
    # Find all class names in the java_code
    class_names = re.findall(class_pattern, java_code_no_comments)
    
    # Extract only the class names from the matches
    return [match[1] for match in class_names]

# Main function to process the folder, translate, and save the output
def main(folder_path=FOLDER_PATH, target_language=TARGET_LANGUAGE):

    # Clean up the output folder
    shutil.rmtree('translated', ignore_errors=True)
    shutil.rmtree('evolved', ignore_errors=True)

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
        
        translated_code, response_text = translate_code(source_code, source_language, target_language)
 
        # Write the transformed code to the output folder
        write_translated_code(output_folder, translated_code, response_text)

if __name__ == '__main__':
    main(FOLDER_PATH, TARGET_LANGUAGE)
