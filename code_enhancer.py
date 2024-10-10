import os
import ollama 

from groq import Groq
from utils import ask_to_ollama, ask_to_groq, extract_java_code, extract_xml_code, get_source_files, get_class_names, LLM_MODE, GROQ_API_KEY

SOURCE_PATH = 'translated'
TARGET_PATH = 'evolved'
SOURCE_LANGUAGE = 'Java'
OUTPUT_SOURCE_CODE = os.path.join(TARGET_PATH, 'src', 'main', 'java')
OUTPUT_TEST_CODE = os.path.join(TARGET_PATH, 'src', 'test', 'java')

client = None
if LLM_MODE == 'GROQ':
    client = Groq(api_key=GROQ_API_KEY)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return None

def enhance_code_with_llm(java_code):
    prompt = f"""
    Improve the following Java code, while maintaining the same functionality.
    Focus on better code structure, formatting, and refactoring, ensuring readability and best practices for object oriented programming.
    It is mandatory not to change the class name and not to remove methods for unit testing. 
    Make sure to import all the necessary libraries.

    Here is the code:
    ```java
    {java_code}
    ```

    Give as output only the code and make a list describing the improvements made.
    """
    if LLM_MODE == 'GROQ':
        return enhance_code_with_groq(prompt)
    else:
        return enhance_code_with_ollama(prompt)

def enhance_code_with_ollama(prompt):
    # Call Ollama and pass the prompt
    result = ollama.chat(model='codellama', messages=[
        {
            'role': 'user',
            'content': prompt + "\n\n" + "Generate pom.xml for this project adding spotbugs version 4.4.2 and junit, org.junit.jupiter and junit-jupiter-engine, with Source option 8 and target option 8. Add the configuration maven-surefire-plugin <include>**/*Test.java</include> and spotbugs"
        }
    ])

    # Extract the translated code from the output
    response_text = result['message'].strip()  # Access 'message' field from Ollama's response
    improved_code = extract_java_code(response_text)
    pom = extract_xml_code(response_text)    
    return improved_code, pom, response_text

def enhance_code_with_groq(prompt):
    # Call Groq's API with the given prompt
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You're an expert Java developer."},
                {"role": "user", "content": prompt},
                {"role": "user", "content": "Generate pom.xml for this project adding spotbugs version 4.4.2 and junit, org.junit.jupiter and junit-jupiter-engine, with Source option 8 and target option 8. Add the configuration maven-surefire-plugin <include>**/*Test.java</include> and spotbugs"}
            ],
            # model="llama-3.1-8b-instant",  # Ensure you use the appropriate Groq model
            model="llama-3.1-70b-versatile",
            temperature=0
        )

        # Extract the response content
        response_text = chat_completion.choices[0].message.content.strip()
        # print(response_text)
        # Extract the Java code using the find() method
        improved_code = extract_java_code(response_text)
        pom = extract_xml_code(response_text)
        
        return improved_code, pom, response_text  # Return both the code and the full response

    except Exception as e:
        print(f"Error during code improvement: {e}")
        return None, None
    
def write_pom_file(input_code):
    file_name = "pom.xml"
    improved_file_path = os.path.join(TARGET_PATH, file_name)
    
    # Write the improved code to the new file
    try:
        with open(improved_file_path, 'w') as file:
            file.write(input_code)
        print(f"Pom file saved at: {improved_file_path}\n")
    except Exception as e:
        print(f"Error writing the file: {e}")

def write_enhanced_source_file(original_file_path, improved_code):
    # Extract file name from the original path and construct the new file path
    file_name = os.path.basename(original_file_path)
    improved_file_path = os.path.join(OUTPUT_SOURCE_CODE, file_name)
    # Write the improved code to the new file
    try:
        with open(improved_file_path, 'w') as file:
            file.write(improved_code)
        print(f"Improved Java file saved at: {improved_file_path}")
    except Exception as e:
        print(f"Error writing the improved file: {e}")

def write_enhanced_test_file(generated_code):
    # Extract file name from the original path and construct the new file path
    file_name = get_class_names(generated_code)[0] +".java"
    output_file_path = os.path.join(OUTPUT_TEST_CODE, file_name)
    
    try:
        with open(output_file_path, 'w') as file:
            file.write(generated_code)
        print(f"Improved Java file saved at: {output_file_path}\n")
    except Exception as e:
        print(f"Error writing the improved file: {e}")

def write_enhancement_summary(original_file_path, response_text, is_test):
    output_folder = OUTPUT_TEST_CODE if is_test else OUTPUT_SOURCE_CODE    
    # Generate a summary file path based on the original file
    file_name = os.path.basename(original_file_path)
    summary_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_improvement_summary.md")

    # Write the summary of improvements
    try:
        with open(summary_file_path, 'w') as summary_file:
            summary_file.write("The following improvements were made by the LLM:\n")
            summary_file.write(response_text)
        print(f"Improvement summary saved at: {summary_file_path}")
    except Exception as e:
        print(f"Error writing the improvement summary: {e}")

def enhance_code(file_path):
    # Step 1: Read the original Java file
    java_code = read_file(file_path)
    if java_code is None:
        return

    # Step 2: enhance the Java code using LLM      
    enhanced_code, pom, response_text = enhance_code_with_llm(java_code)
    if enhanced_code is None:
        print("No valid improvements were generated.")
        return

    # Step 3: Save the improved Java code to the 'evolved' folder
    write_enhanced_source_file(file_path, enhanced_code)

    # Step 4: Write the improvement summary to a separate text file
    write_enhancement_summary(file_path, response_text, False)

    # Step 5: Write the pom
    write_pom_file(pom)

def generate_unit_tests(source_code):
    system_prompt = f"You will act as a software tester specializing in JUnit. I will provide you with a specific test scenario, and you need to generate a corresponding test suite using JUnit. The test suite should follow these guidelines: only test public methods, only access public variables and exclude testing internal private classes."
    prompt = f"Generate 5 test suite in Junit for the following class:\n\n{source_code}\n\n Don't generate test that requires user input and don't access to private methods or fields. "

    if LLM_MODE == 'GROQ':
        # Translate the code using Groq 
        return ask_to_groq(system_prompt, prompt)
    else:
        # Translate the code using Ollama
        return ask_to_ollama(system_prompt + prompt)

def main():
    # setup
    if not os.path.exists(OUTPUT_SOURCE_CODE):
        os.makedirs(OUTPUT_SOURCE_CODE)
    if not os.path.exists(OUTPUT_TEST_CODE):
        os.makedirs(OUTPUT_TEST_CODE)

    source_files = get_source_files(SOURCE_PATH, ('.java'))
    for source_file in source_files:
        print("✨ Enhancing ", source_file)
        enhance_code(source_file)

    # Get all enhanced files that need tests
    source_files = get_source_files(OUTPUT_SOURCE_CODE, ('.java'))

    for file_path in source_files:
        print(f"🧪 Generating tests for {file_path}")

        # Read the source code
        with open(file_path, 'r') as f:
            source_code = f.read()

        generated_code, response_text = generate_unit_tests(source_code)

        write_enhancement_summary(file_path, response_text, True)
        # Write the transformed code to the output folder
        write_enhanced_test_file(generated_code)

if __name__ == "__main__":
    main()