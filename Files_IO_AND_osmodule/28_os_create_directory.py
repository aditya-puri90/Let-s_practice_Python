'''Q28. Create a Directory

Create a folder called 'PythonPractice' safely using os.mkdir().
'''

import os

dir_name = "PythonPractice"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created successfully!")
else:
    print(f"Directory '{dir_name}' already exists.")
