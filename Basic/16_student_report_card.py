'''Student Result Data

Take the following from the user:

Name
Age
Marks in Python
Marks in SQL
Marks in Maths

Then print:

Student Name:
Age:
Python Marks:
SQL Marks:
Maths Marks:
Total:
Average:'''

name= str(input("Enter the Student name:"))
age = int(input("ENter the Student Age:"))
python =int(input("Enter the marks in python:"))
sql = int(input("Enter the marks in sql:" ))
math = int(input("ENter the marks in maths:"))

total_marks = python + sql + math
average_marks = total_marks / 3

print("\nStudent Name:", name)
print("Age:", age)
print("Python Marks:", python)
print("SQL Marks:", sql)
print("Maths Marks:", math)
print("Total:", total_marks)
print("Average:", average_marks)