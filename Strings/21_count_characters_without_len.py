'''Q21. Character Counter

Take a string and count the total number of characters without using len().

💡 Use a loop.
'''

text = input("Enter string: ")
total = 0

for char in text:
    total += 1

print("Total characters in string:", total)
