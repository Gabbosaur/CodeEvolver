import ollama  # Ensure the Ollama module is installed and running locally
import os
from groq import Groq
import re

LLM_MODE = os.getenv('LLM_MODE')


client = None
if LLM_MODE == 'GROQ':
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
    

def extract_java_code(text):
    return extract_code(text, 'java')
    
def extract_xml_code(text):
    return extract_code(text, 'xml')
    
def extract_code(text, language):
    start = text.find("```" + language) + len("```" + language)
    end = text.find("```", start)

    if start != -1 and end != -1:
        # Extract the code selected and remove leading/trailing whitespaces
        code = text[start:end].strip()
        return code
    else:
        print(f"No valid {language} code block found in the text.")
        return None

# Function to get files based on extensions
def get_source_files(folder_path, extensions):
    source_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extensions):
                source_files.append(os.path.join(root, file))
    return source_files


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
        print(system_prompt)
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
