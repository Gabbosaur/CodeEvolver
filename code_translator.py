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

    # new_text = text[end+1:]
    # start_test = new_text.find("```java") + len("```java")
    # end_test = new_text.find("```", start_test)

    if start != -1 and end != -1:
        # Extract the Java code and remove leading/trailing whitespaces
        java_code_extracted = text[start:end].strip()
        # java_test_extracted = new_text[start_test:end_test].strip()
        return java_code_extracted#, java_test_extracted
    else:
        print("No valid Java code block found in the text.")
        return None


def to_pascal_case(s: str) -> str:
    # Split the string by spaces or underscores and capitalize each word
    return ''.join(word.capitalize() for word in s.replace('_', ' ').split())

def translate_code_with_groq(source_code, source_language, file_path, is_source=True,target_language='Java'):
    if is_source:
        prompt = f"Translate the following from {source_language} to {target_language}:\n\n{source_code}"
    else:
        prompt = f"Generate 5 test suite in Junit for the following class:\n\n{source_code}\n\n Don't generate test that requires user input. "
    # Call Groq's API with the given prompt
    try:
        if is_source:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": f"I want you to act as a code translator. I will provide you with code in a specific source language, and I want you to translate it into a different target language. The translation should maintain the same functionalities as the original code, but using an object-oriented approach. Additionally, you should include plenty of comments to enhance readability. After that remember to add public methods for future unit testing. Finally, rename the class name according to {to_pascal_case(Path(file_path).stem)}. "},
                    {"role": "user", "content": prompt}
                ],
                #model="llama-3.1-8b-instant",  # Ensure you use the appropriate Groq model
                # model="llama3-8b-8192",
                model="llama-3.1-70b-versatile",
                #model="mixtral-8x7b-32768",
                temperature=0
            )
        else:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": f"You will act as a software tester specializing in JUnit. I will provide you with a specific test scenario, and you need to generate a corresponding test suite using JUnit. The test suite should follow these guidelines: rename the class name as {to_pascal_case(Path(file_path).stem)}Test, only test public methods, only access public variables and exclude testing internal private classes. If you're unsure, simply respond with \"I don\'t know\"."},
                    {"role": "user", "content": prompt}
                ],
                #model="llama3-groq-70b-8192-tool-use-preview",
                #model="llama-3.1-8b-instant",  # Ensure you use the appropriate Groq model
                # model="llama3-8b-8192",
                model="llama-3.1-70b-versatile",
                #model="mixtral-8x7b-32768",
                temperature=0
            )
        # Extract the response content
        response_text = chat_completion.choices[0].message.content.strip()
        print(response_text)
        # Extract the Java code using the find() method
        #improved_code, test_suite = extract_java_code(response_text)
        improved_code = extract_java_code(response_text)

        return improved_code, response_text  # Return both the code and the full response
        # return improved_code, test_suite, response_text  # Return both the code and the full response

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
#def write_transformed_code(output_folder, file_path, transformed_code, test_suite):
def write_transformed_code(output_folder, file_path, transformed_code, is_source, response_text):
    os.makedirs(output_folder, exist_ok=True)
    if is_source: 
        file_name = to_pascal_case(Path(file_path).stem) + ".java"
    else:
        file_name = to_pascal_case(Path(file_path).stem) + "Test.java"
    output_path = os.path.join(output_folder, file_name)        
    #output_path_test = os.path.join(output_folder, file_name_test)
    
    if transformed_code is None:
        with open(output_path, 'w') as f:
            f.write(response_text)
    else:
        with open(output_path, 'w') as f:
            f.write(transformed_code)

    # with open(output_path_test, 'w') as f:
    #     f.write(test_suite)
    
    print(f"Translated code written to {output_path}")

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

        if LLM_MODE == 'GROQ':
            # Translate the code using Groq 
            # translated_code, test_suite, response_text = translate_code_with_groq(source_code, source_language, file_path, target_language)
            translated_code, response_text = translate_code_with_groq(source_code, source_language, file_path, True, target_language)

        else:
            # TODO ollama should have the same behavior as groq
            # Translate the code using Ollama
            translated_code = translate_code_with_ollama(source_code, source_language, target_language)
        
        # Write the transformed code to the output folder
        write_transformed_code(output_folder, file_path, translated_code, True, None)
        # write_transformed_code(output_folder, file_path, translated_code, test_suite)

    # Get all files that need tests
    source_files = get_source_files(output_folder, ('.py', '.cob', '.cbl', '.java'))

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
            # translated_code, test_suite, response_text = translate_code_with_groq(source_code, source_language, file_path, target_language)
            translated_code, response_text = translate_code_with_groq(source_code, source_language, file_path, False, target_language)

        else:
            # TODO ollama should have the same behavior as groq
            # Translate the code using Ollama
            translated_code = translate_code_with_ollama(source_code, source_language, target_language)
        
        # Write the transformed code to the output folder
        write_transformed_code(output_folder, file_path, translated_code, False, response_text)
        # write_transformed_code(output_folder, file_path, translated_code, test_suite)

# Run the main function with the hardcoded folder path and target language
if __name__ == '__main__':
    main(FOLDER_PATH, TARGET_LANGUAGE)
