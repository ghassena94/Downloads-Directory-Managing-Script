import os # This module provides a way of using operating system dependent functionality like reading or writing to the file system.
import shutil # This module offers a number of high-level operations on files and collections of files, including copying and moving files.

# Define the directory to organize
directory_to_organize = "/Users/ghassen/Downloads"

# Define your organization rules
organization_rules = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.heic'],
    'Documents': ['.docx', '.txt', '.xlsx'],
    'PDFs': ['.pdf'],
    'Music': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Programing_Documents': ['.html', '.class', 'jar'],
    'ApplicationsDownload': ['.dmg', '.pkg', '.app']
}


def organize_files(directory):
    for filename in os.listdir(directory): # Lists all the files and directories in the given directory.
        # Skip directories
        file_path = os.path.join(directory, filename)
            # Check if the current item is a directory and if it's an application bundle
        if os.path.isdir(file_path):
            if file_path.endswith('.app'):
                    destination_dir = 'ApplicationsDownload'
            else:
                    continue
        else:
                file_ext = os.path.splitext(filename)[1].lower()
                destination_dir = None

                for folder, extensions in organization_rules.items():
                    if file_ext in extensions:
                        destination_dir = folder
                        break

        if destination_dir:
            destination_path = os.path.join(directory, destination_dir)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            shutil.move(os.path.join(directory, filename), os.path.join(destination_path, filename))
            # Moves the file to the destination directory.


if __name__ == "__main__":
    organize_files(directory_to_organize)
