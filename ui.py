import streamlit as st
import tkinter as tk # sudo apt-get install python3-tk
from tkinter import filedialog
import os

def select_folder():
    # Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()
    
    # Open the folder selection dialog
    folder_path = filedialog.askdirectory()
    root.destroy()
    return folder_path

def main():
    st.title("Folder Selection Interface")

    # Create a container for the folder selection
    selection_container = st.container()

    with selection_container:
        st.markdown("""
        ### Select Folder
        Click the button below to choose a folder from your computer
        """)

        # Create a button to trigger folder selection
        if st.button("Select Folder"):
            folder_path = select_folder()

            if folder_path:
                # Store the folder path in session state so it persists
                st.session_state['folder_path'] = folder_path
                st.success(f"Folder selected: {folder_path}")

                # Display the contents of the folder
                files = os.listdir(folder_path)
                st.write(f"Number of files/folders detected: {len(files)}")

                st.write("Contents of the folder:")
                for item in files:
                    full_path = os.path.join(folder_path, item)
                    if os.path.isfile(full_path):
                        st.write(f"📄 {item}")
                    else:
                        st.write(f"📁 {item}")
            else:
                st.warning("No folder selected")

        # Display the currently selected folder path if it exists
        if 'folder_path' in st.session_state:
            st.info(f"Currently selected folder: {st.session_state['folder_path']}")

if __name__ == "__main__":
    main()