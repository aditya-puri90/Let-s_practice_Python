'''Q24. Calculate Average Marks

Read the CSV file and calculate the average marks of all students.
'''

import csv

with open("students.csv", "r") as f:
    content = csv.reader(f)
    next(content)  # Skip header

    total_marks = 0
    count = 0

    for row in content:
        marks = int(row[3])
        total_marks += marks
        count += 1

average_marks = total_marks / count if count > 0 else 0
print(f"Average marks of all students: {average_marks:.2f}")
