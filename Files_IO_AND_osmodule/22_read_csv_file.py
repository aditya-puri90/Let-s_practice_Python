'''Q22. Read CSV File

Read students.csv and print each student's information formatted.
'''

import csv

with open("students.csv", "r") as f:
    content = csv.reader(f)
    header = next(content)
    print("Columns:", ", ".join(header))

    for row in content:
        name, age, course, marks = row
        print(f"Name: {name}, Age: {age}, Course: {course}, Marks: {marks}")
