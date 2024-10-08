import os
import shutil

from utlls import ask_to_ollama, ask_to_groq, get_class_names, get_source_files, detect_language, LLM_MODE

# Hardcoded folder path and target language
FOLDER_PATH = 'legacy_project'  # <-- Set your folder path here
TARGET_PATH = 'translated'
TARGET_LANGUAGE = 'Java'  # Default target language for translation is set to Java

# Function to write the translated code to a file
def write_translated_code(transformed_code, response_text):
    os.makedirs(TARGET_PATH, exist_ok=True)
    file_name = get_class_names(transformed_code)[0] + ".java"
    output_path = os.path.join(TARGET_PATH, file_name)  
    
    with open(output_path, 'w') as f:
        f.write(transformed_code)

    print(f"Translated code written to {output_path}")

def translate_code(source_code, source_language, target_language):
    
    system_prompt = f"I want you to act as a code translator. I will provide you with code in a specific source language, and I want you to translate it into a different target language. The translation should maintain the same functionalities as the original code, but using an object-oriented approach. Additionally, you should include plenty of comments to enhance readability. After that remember to add public methods for future unit testing.\n\n"
    prompt = f"Translate the following from {source_language} to {target_language}:\n\n{source_code}"

    if LLM_MODE == 'GROQ':
        print(f"Using Groq")
        # Translate the code using Groq 
        return ask_to_groq(system_prompt, prompt)
    else:
        print(f"Using Ollama")
        # Translate the code using Ollama
        return ask_to_ollama(system_prompt + prompt)

# Main function to process the folder, translate, and save the output
def main(folder_path=FOLDER_PATH, target_language=TARGET_LANGUAGE):

    # Clean up the output folder
    shutil.rmtree('translated', ignore_errors=True)
    shutil.rmtree('evolved', ignore_errors=True)

    # Get all files that need to be processed (Python, COBOL, Java)
    source_files = get_source_files(folder_path, ('.py', '.cob', '.cbl', '.java'))

    # Output folder for transformed/translated files
    # output_folder = os.path.join()

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
        write_translated_code(translated_code, response_text)

if __name__ == '__main__':
    main(FOLDER_PATH, TARGET_LANGUAGE)
