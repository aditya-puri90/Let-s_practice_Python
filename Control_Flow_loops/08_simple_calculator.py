'''Q8. Simple Calculator

Take two numbers and an operator (+, -, *, /).
Use if-elif-else to perform the selected operation.'''

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator!")
