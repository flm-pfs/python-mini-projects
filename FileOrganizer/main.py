import os
import shutil


def organize_files(directory):
    # Define file types and their corresponding extensions
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.doc', '.docx', '.pdf', '.txt'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav'],
        'Others': []
    }

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            moved = False
            # Check the file extension and move it to the corresponding category directory
            for category, extensions in file_types.items():
                if ext in extensions:
                    category_dir = os.path.join(directory, category)
                    if not os.path.exists(category_dir):
                        os.makedirs(category_dir)
                    shutil.move(file_path, os.path.join(
                        category_dir, filename))
                    moved = True
                    break
            # If the file doesn't match any category, move it to the 'Others' directory
            if not moved:
                others_dir = os.path.join(directory, 'Others')
                if not os.path.exists(others_dir):
                    os.makedirs(others_dir)
                shutil.move(file_path, os.path.join(others_dir, filename))


def main():
    # Get the directory path from user input
    directory = input("Enter the directory path to organize: ")
    if os.path.exists(directory):
        # Organize the files in the directory
        organize_files(directory)
        print("Files organized successfully.")
    else:
        print("Directory does not exist.")


if __name__ == "__main__":
    main()
