'''Q7. Count Lines

Create a program that counts how many lines are present in a text file.
'''

with open("students.txt", "r") as f:
    lines = f.readlines()

line_count = len(lines)
print("Total number of lines:", line_count)
