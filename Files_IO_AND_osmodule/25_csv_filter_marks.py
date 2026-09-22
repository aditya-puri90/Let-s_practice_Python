'''Q25. Filter CSV Records

Read students.csv and display only students whose marks are greater than 80.
'''

import csv

with open("students.csv", "r") as f:
    content = csv.reader(f)
    next(content)  # Skip header

    print("Students with marks greater than 80:")
    for row in content:
        name, age, course, marks = row
        if int(marks) > 80:
            print(f"Name: {name}, Age: {age}, Course: {course}, Marks: {marks}")
