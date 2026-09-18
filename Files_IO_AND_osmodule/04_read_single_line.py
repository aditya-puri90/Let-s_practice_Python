'''Q4. Read One Line

Create a file containing 5 different lines and use readline() to read only the first line.
'''

with open("file.txt", "w") as f:
    f.write("Line 1: Python is fun.\n")
    f.write("Line 2: I am learning file handling.\n")
    f.write("Line 3: Data Science uses Python.\n")
    f.write("Line 4: Practice makes perfect.\n")
    f.write("Line 5: Keep coding daily.\n")

with open("file.txt", "r") as f:
    first_line = f.readline()
    print("First line:", first_line.strip())
