'''Q23. Find Highest Marks

Using the CSV file students.csv, find the student who scored the highest marks.
'''

import csv

with open("students.csv", "r") as f:
    content = csv.reader(f)
    next(content)  # Skip header

    highest_marks = -1
    top_student = None

    for row in content:
        name, age, course, marks = row
        marks = int(marks)

        if marks > highest_marks:
            highest_marks = marks
            top_student = (name, age, course, marks)

if top_student:
    print(f"Top student: {top_student[0]}, Age: {top_student[1]}, Course: {top_student[2]}, Marks: {top_student[3]}")
