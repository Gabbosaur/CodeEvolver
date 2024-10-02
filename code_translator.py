import os
import ollama  # Ensure the Ollama module is installed and running locally
from pathlib import Path

# Hardcoded folder path and target language
FOLDER_PATH = '/home/ubuntu/Projects/hackathon/CodeEvolver/legacyproject/'  # <-- Set your folder path here
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
def write_transformed_code(output_folder, file_path, transformed_code):
    os.makedirs(output_folder, exist_ok=True)
    file_name = Path(file_path).stem + ".java"
    output_path = os.path.join(output_folder, file_name)
    
    with open(output_path, 'w') as f:
        f.write(transformed_code)
    
    print(f"Translated code written to {output_path}")

# Main function to process the folder, translate, and save the output
def main(folder_path, target_language='Java'):
    # Get all files that need to be processed (Python, COBOL, Java)
    source_files = get_source_files(folder_path, ('.py', '.cob', '.cbl', '.java'))
    
    # Output folder for transformed files
    output_folder = os.path.join(folder_path, 'transformed')

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

        # Translate the code using the Ollama model
        translated_code = translate_code_with_ollama(source_code, source_language, target_language)
        
        # Write the transformed code to the output folder
        write_transformed_code(output_folder, file_path, translated_code)

# Run the main function with the hardcoded folder path and target language
if __name__ == '__main__':
    main(FOLDER_PATH, TARGET_LANGUAGE)
