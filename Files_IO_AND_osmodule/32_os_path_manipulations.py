'''Q32. OS Path Manipulations

Demonstrate os.path.join, dirname, basename, and splitext operations.
'''

import os

sample_path = os.path.join("Files_IO_AND_osmodule", "data", "report.csv")

print("Joined Path :", sample_path)
print("Directory   :", os.path.dirname(sample_path))
print("Basename    :", os.path.basename(sample_path))
root, ext = os.path.splitext(sample_path)
print("Root Name   :", root)
print("Extension   :", ext)
