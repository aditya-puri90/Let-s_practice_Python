'''Q28. Remove Duplicate Characters ⭐⭐⭐

Take a string like:
"programming"

and create a string containing each character only once.

Expected conceptually:
"progamin"

Try doing it without using set().
'''

text = input("Enter string: ")
result = ""

for char in text:
    if char not in result:
        result += char

print("Result =", result)
