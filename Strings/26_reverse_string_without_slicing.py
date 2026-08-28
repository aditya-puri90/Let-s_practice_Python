'''Q26. Reverse Without Slicing ⭐⭐⭐

Reverse a string without using [::-1].

Example:
Input: Python
Output: nohtyP

Use a loop.
'''

text = input("Enter string: ")
reverse = ""

for char in text:
    reverse = char + reverse

print("Output:", reverse)
