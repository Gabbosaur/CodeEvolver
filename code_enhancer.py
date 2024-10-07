import os
import re
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

LLM_MODE = os.getenv('LLM_MODE')
FOLDER_PATH = './translated/'  # <-- Set your folder path here


client = None
if LLM_MODE == 'GROQ':
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def read_java_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return None

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
    
def extract_xml_code(text):
    start = text.find("```xml") + len("```xml")
    end = text.find("```", start)

    if start != -1 and end != -1:
        # Extract the Java code and remove leading/trailing whitespaces
        code = text[start:end].strip()
        return code
    else:
        print("No valid Java code block found in the text.")
        return None

def improve_code_with_groq(java_code):
    prompt = f"""
    Improve the following Java code, while maintaining the same functionality.
    Focus on better code structure, formatting, and refactoring, ensuring readability and best practices for object oriented programming.
    It is mandatory not to change the class name and not to remove methods for unit testing.

    Here is the code:
    ```java
    {java_code}
    ```

    Give as output only the code and make a list describing the improvements made.
    """

    # Call Groq's API with the given prompt
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You're an expert Java developer."},
                {"role": "user", "content": prompt},
                {"role": "user", "content": "Generate pom.xml for this project adding spotbugs version 4.4.2 and junit, org.junit.jupiter and junit-jupiter-engine, with Source option 8 and target option 8."}
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
    
def write_pom_file(input_code, is_test):
    # Create 'evolved' folder if it doesn't exist
    output_folder = "evolved"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder + "/src/test/java")
        os.makedirs(output_folder + "/src/main/java")
    
    file_name = "pom.xml"
    improved_file_path = os.path.join(output_folder, file_name)
    
    # Write the improved code to the new file
    try:
        with open(improved_file_path, 'w') as file:
            file.write(input_code)
        print(f"Pom file saved at: {improved_file_path}")
    except Exception as e:
        print(f"Error writing the file: {e}")

def write_improved_java_file(original_file_path, improved_code, is_test):
    # Create 'evolved' folder if it doesn't exist
    output_folder = "evolved"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder + "/src/test/java")
        os.makedirs(output_folder + "/src/main/java")
    if is_test:
        output_folder = "evolved/src/test/java"
    else:
        output_folder = "evolved/src/main/java"
    
    # Extract file name from the original path and construct the new file path
    file_name = os.path.basename(original_file_path)
    improved_file_path = os.path.join(output_folder, file_name)
    
    # Write the improved code to the new file
    try:
        with open(improved_file_path, 'w') as file:
            file.write(improved_code)
        print(f"Improved Java file saved at: {improved_file_path}")
    except Exception as e:
        print(f"Error writing the improved file: {e}")

def remove_multiple_newlines(input_string: str) -> str:
    # Use regex to replace multiple newlines with a single newline
    return re.sub(r'\n+', '\n', input_string).strip()

def write_improvement_summary(original_file_path, response_text, is_test):
    # Create 'evolved' folder if it doesn't exist
    output_folder = "evolved"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder + "/src/test/java")
        os.makedirs(output_folder + "/src/main/java")
    if is_test:
        output_folder = "evolved/src/test/java"
    else:
        output_folder = "evolved/src/main/java"
    
    # Generate a summary file path based on the original file
    file_name = os.path.basename(original_file_path)
    summary_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_improvement_summary.md")

    # Write the summary of improvements
    try:
        with open(summary_file_path, 'w') as summary_file:
            summary_file.write("The following improvements were made by the LLM:\n")
            summary_file.write(response_text)
            # summary_file.write(remove_multiple_newlines(response_text.split("```")[-1]))
        print(f"Improvement summary saved at: {summary_file_path}")
    except Exception as e:
        print(f"Error writing the improvement summary: {e}")

def improve_java_file(file_path):
    """Main function that reads, improves, and writes the Java file."""
    # Step 1: Read the original Java file
    java_code = read_java_file(file_path)
    if java_code is None:
        return
    
    # Step 2: Improve the Java code using Groq LLM
    improved_code, pom, response_text = improve_code_with_groq(java_code)
    if improved_code is None:
        print("No valid improvements were generated.")
        return
    
    is_test = "Test" in Path(file_path).stem

    # Step 3: Save the improved Java code to the 'evolved' folder
    write_improved_java_file(file_path, improved_code, is_test)
    
    # Step 4: Write the improvement summary to a separate text file
    write_improvement_summary(file_path, response_text, is_test)

    # Step 5: Write the pom
    if not is_test:
        write_pom_file(pom, is_test)

# Function to get files based on extensions
def get_source_files(folder_path, extensions):
    source_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extensions):
                source_files.append(os.path.join(root, file))
    return source_files

def main(folder_path=FOLDER_PATH):
    source_files = get_source_files(folder_path, ('.java'))
    for source_file in source_files:
        improve_java_file(source_file)

if __name__ == "__main__":
    main()