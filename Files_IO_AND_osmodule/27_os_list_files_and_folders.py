'''Q27. List Files and Folders

Display all files and folders present in the current directory using os.listdir().
'''

import os

files = os.listdir(".")
print("Directory entries count:", len(files))
print("Files and folders:", files)
