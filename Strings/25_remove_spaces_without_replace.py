'''Q25. Remove Spaces

Take a sentence and create a new string without spaces.

Example:
Input: Python is easy
Output: Pythoniseasy

Try solving it using a loop.
'''

text = input("Enter string: ")
result = ""

for char in text:
    if char != " ":
        result += char

print("Output:", result)
