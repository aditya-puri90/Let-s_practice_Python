'''Q6. Read Using a Loop

Read students.txt line by line using a for loop.
'''

with open("students.txt", "r") as f:
    for line in f:
        print("Student:", line.strip())
