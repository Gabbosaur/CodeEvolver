import streamlit as st
import os
import zipfile
import tempfile
import requests
from io import BytesIO

# Define the path for the legacy_project folder
LEGACY_PROJECT_FOLDER = "legacy_project"
EVOLVED_PROJECT_FOLDER = "evolved"
EVOLVE_API_URL = "http://localhost:8000/evolve/"

# Ensure the folder exists
os.makedirs(LEGACY_PROJECT_FOLDER, exist_ok=True)

st.set_page_config(
    page_title="CodeEvolver", 
    page_icon=os.path.join("resources", "icon.png")
)


def save_uploaded_file(uploaded_file):
    os.makedirs(LEGACY_PROJECT_FOLDER, exist_ok=True)
    save_path = os.path.join(LEGACY_PROJECT_FOLDER, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

def create_zip_of_folder(folder_path):
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))
    zip_buffer.seek(0)
    return zip_buffer

def main():
    st.title("CodeEvolver")

    # Option for user to choose between folder and specific files.
    upload_option = st.radio(
        "Select what you want to upload:",
        ("Upload ZIP", "Upload Specific Files")
    )
    
    uploaded_files = None
    zip_buffer = None

    if upload_option == "Upload ZIP":
        uploaded_files = st.file_uploader(
            "Upload a ZIP file containing Cobol files:",
            type="zip",
            accept_multiple_files=False
        )

        if uploaded_files:
            # Save the uploaded ZIP file to the legacy_project folder
            zip_save_path = save_uploaded_file(uploaded_files)
            st.write(f"ZIP file saved to: {zip_save_path}")

            # Extract the ZIP file to a temporary directory for processing
            with tempfile.TemporaryDirectory() as temp_dir:
                with zipfile.ZipFile(zip_save_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)
                
                st.write("Uploaded folder content:")
                st.write(os.listdir(temp_dir))
                data = {"url": temp_dir}

                # Process the extracted folder
                if st.button("Process Folder"):
                    with st.spinner("Processing the folder..."):
                        try:
                            response = requests.post(EVOLVE_API_URL, json=data)
                            response.raise_for_status()
                            output = response.json()
                            st.success(f'Code successfully translated and enhanced!\nCheck pipeline status {output}' , icon="✅")

                            # Create the ZIP buffer of the processed folder
                            zip_buffer = create_zip_of_folder(EVOLVED_PROJECT_FOLDER)

                        except requests.exceptions.RequestException as e:
                            output = f"Error during API call: {str(e)}"
                            st.error(output, icon="🚨")

    elif upload_option == "Upload Specific Files":
        uploaded_files = st.file_uploader(
            "Upload one or multiple files:",
            type=["cob", "cbl"],
            accept_multiple_files=True
        )

        if uploaded_files:
            st.write(f"{len(uploaded_files)} file(s) uploaded.")
            # Save and display uploaded files
            saved_files = [save_uploaded_file(file) for file in uploaded_files]
            data = {"url": LEGACY_PROJECT_FOLDER}

            # Process the files
            if st.button("Process Files"):
                with st.spinner("Processing files..."):
                    try:
                        response = requests.post(EVOLVE_API_URL, json=data)
                        response.raise_for_status()
                        output = response.json()[0]
                        st.success(f'Code successfully translated and enhanced!', icon="✅")
                        st.markdown(f'Check pipeline status [here]({output})')
                        
                        # Create the ZIP buffer of the processed folder
                        zip_buffer = create_zip_of_folder(EVOLVED_PROJECT_FOLDER)

                    except requests.exceptions.RequestException as e:
                        output = f"Error during API call: {str(e)}"
                        st.error(output, icon="🚨")

    # Show the download button if the zip_buffer is created
    if zip_buffer:
        st.download_button(
            label="Download Processed Files as ZIP",
            data=zip_buffer,
            file_name="CodeEvolver_evolved_legacy_project.zip",
            mime="application/zip"
        )

if __name__ == "__main__":
    main()
