import os
import shutil

def copy_files_recursive(source_dir, destination_dir):
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Copy the entire directory tree
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

    print(f'All files and directories copied from {source_dir} to {destination_dir}')


def remove_except(source_dir, exclude_dir, exclude_file):
    """Remove all files and directories in source_dir except for exclude_dir and exclude_file."""
    # Walk through the directory
    for root, dirs, files in os.walk(source_dir, topdown=False):
        # Remove files that are not the excluded file
        for name in files:
            file_path = os.path.join(root, name)
            if name != exclude_file:
                print(f'Removing file: {file_path}')
                os.remove(file_path)

        # Remove directories if they are not the excluded directory
        for name in dirs:
            dir_path = os.path.join(root, name)
            if name != exclude_dir:
                print(f'Removing directory: {dir_path}')
                shutil.rmtree(dir_path)

    print(f'Finished removing files and directories in {source_dir}, except for {exclude_dir} and {exclude_file}')


def main():
    source_dir = 'evolved'
    destination_dir = 'jenkins_home/workspace/test'
    
    exclude_dir = 'builds'     # The directory to exclude
    exclude_file = 'config.xml'     # The file to exclude

    # clean
    remove_except(destination_dir, exclude_dir, exclude_file)

    # copy
    copy_files_recursive(source_dir, destination_dir)

if __name__ == '__main__':
    main()
