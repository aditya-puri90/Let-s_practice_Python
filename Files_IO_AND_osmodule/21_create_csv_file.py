'''Q21. Create a CSV File

Create students.csv with columns: Name, Age, Course, Marks using csv.writer.
'''

import csv

students = [
    ["Name", "Age", "Course", "Marks"],
    ["Aditya", 20, "Python", 85],
    ["Rahul", 21, "SQL", 78],
    ["Amit", 22, "Statistics", 90],
    ["Rohan", 23, "ML", 88],
    ["Pooja", 21, "Power BI", 92]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("students.csv created successfully!")
