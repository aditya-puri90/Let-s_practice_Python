'''Q29. Mini File Organizer

Create a Python program that organizes files into folders based on their extensions.
'''

import os
import shutil

def organize_files(directory="."):
    folders = {
        ".txt": "Text_Files",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".csv": "CSV_Files",
        ".pdf": "PDF_Documents"
    }

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    organized_count = 0

    for file in files:
        _, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext in folders and not file.endswith(".py"):
            folder_name = os.path.join(directory, folders[ext])
            os.makedirs(folder_name, exist_ok=True)

            src = os.path.join(directory, file)
            dst = os.path.join(folder_name, file)
            shutil.copy(src, dst)
            print(f"Organized: {file} -> {folders[ext]}/")
            organized_count += 1

    print(f"File organization complete. {organized_count} files organized.")

if __name__ == "__main__":
    organize_files(".")
