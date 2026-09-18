'''Q5. Read All Lines

Create a file 'students.txt' containing names and use readlines() to read all lines into a list.
'''

with open("students.txt", "w") as f:
    f.write("Aditya\n")
    f.write("Rahul\n")
    f.write("Amit\n")
    f.write("Rohan\n")
    f.write("Akash\n")

with open("students.txt", "r") as f:
    lines = f.readlines()

print("All lines as a list:", lines)
