'''Q30. Check Path Existence and File Type

Check if a given path exists and whether it is a file or a directory using os.path.
'''

import os

test_paths = ["notes.txt", "students.csv", "PythonPractice", "non_existent.txt"]

for path in test_paths:
    exists = os.path.exists(path)
    is_file = os.path.isfile(path) if exists else False
    is_dir = os.path.isdir(path) if exists else False

    print(f"Path: '{path}' | Exists: {exists} | Is File: {is_file} | Is Dir: {is_dir}")
