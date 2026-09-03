'''
Q29. Student marks dictionary ⭐⭐

Create:

marks = {
    "Python": 85,
    "SQL": 90,
    "Statistics": 78,
    "Data Science": 88
}

Write a program to:

Print all subjects.
Print all marks.
Calculate total marks.
Calculate percentage.
Find the subject with the highest marks.
'''
marks = {
    "Python": 85,
    "SQL": 90,
    "Statistics": 78,
    "Data Science": 88
}

# 1. Print subjects
print("Subjects:")
for subject in marks.keys():
    print(subject)


# 2. Print marks
print("\nMarks:")
for mark in marks.values():
    print(mark)


# 3. Calculate total
total = sum(marks.values())

print("\nTotal:", total)


# 4. Calculate percentage
percentage = total / len(marks)

print("Percentage:", percentage)


# 5. Find highest marks
highest_subject = max(marks, key=marks.get)

print("Highest Marks Subject:", highest_subject)
print("Highest Marks:", marks[highest_subject])

