'''Take marks of 3 subjects as input and calculate:

Total marks
Average marks

Make sure the inputs are converted to the appropriate numeric type.'''

python = int(input("Enter the python marks:"))
sql = int(input("Enter the sql marks:"))
math = int(input("Enter the math marks:"))

total_marks = python + sql + math
Avg_marks = total_marks / 3

print("Total marks =", total_marks , "Average Marks =", Avg_marks)