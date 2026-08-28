'''Q23. Count Digits in a String

Take a string such as:
"Python12345"

Count how many digits are present.

Expected:
Digits = 5
'''

text = input("Enter string: ")

count = 0
for char in text:
    if char.isdigit():
        count += 1

print("Digits =", count)
