'''Q31. Rename and Remove Files

Demonstrate file renaming and deletion using os.rename() and os.remove().
'''

import os

temp_file = "temp_demo.txt"
renamed_file = "renamed_demo.txt"

# Step 1: Create a temp file
with open(temp_file, "w") as f:
    f.write("Temporary demonstration content.\n")
print(f"1. Created '{temp_file}'.")

# Step 2: Rename the file
if os.path.exists(temp_file):
    if os.path.exists(renamed_file):
        os.remove(renamed_file)
    os.rename(temp_file, renamed_file)
    print(f"2. Renamed '{temp_file}' -> '{renamed_file}'.")

# Step 3: Remove the renamed file
if os.path.exists(renamed_file):
    os.remove(renamed_file)
    print(f"3. Deleted '{renamed_file}' successfully.")
