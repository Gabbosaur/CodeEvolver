import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

LLM_MODE = os.getenv('LLM_MODE')


client = None
if LLM_MODE == 'GROQ':
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

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

def improve_code_with_groq(java_code):
    prompt = f"""
    Improve the following Java code, while maintaining the same functionality.
    Focus on better code structure, formatting, and refactoring, ensuring readability and best practices.

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
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",  # Ensure you use the appropriate Groq model
            temperature=0
        )

        # Extract the response content
        response_text = chat_completion.choices[0].message.content.strip()

        # Extract the Java code using the find() method
        improved_code = extract_java_code(response_text)
        return improved_code, response_text  # Return both the code and the full response

    except Exception as e:
        print(f"Error during code improvement: {e}")
        return None, None

def write_improved_java_file(original_file_path, improved_code):
    # Create 'evolved' folder if it doesn't exist
    output_folder = "evolved"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
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

def write_improvement_summary(original_file_path, response_text):
    # Create 'evolved' folder if it doesn't exist
    output_folder = "evolved"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Generate a summary file path based on the original file
    file_name = os.path.basename(original_file_path)
    summary_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_improvement_summary.txt")

    # Write the summary of improvements
    try:
        with open(summary_file_path, 'w') as summary_file:
            summary_file.write("The following improvements were made by Groq's LLM:\n\n")
            summary_file.write(response_text)
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
    improved_code, response_text = improve_code_with_groq(java_code)
    if improved_code is None:
        print("No valid improvements were generated.")
        return
    
    # Step 3: Save the improved Java code to the 'evolved' folder
    write_improved_java_file(file_path, improved_code)
    
    # Step 4: Write the improvement summary to a separate text file
    write_improvement_summary(file_path, response_text)

def main(java_file_path = "/home/ubuntu/Projects/hackathon/CodeEvolver/translated/TrimethiusCipher.java" ):
    improve_java_file(java_file_path)

if __name__ == "__main__":
    main()