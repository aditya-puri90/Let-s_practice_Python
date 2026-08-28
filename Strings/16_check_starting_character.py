'''Q16. Check Starting Character

Take a string and check whether it starts with "A".

Use .startswith().
'''

text = input("Enter string: ")
char = "A"

if text.startswith(char):
    print("Starts with", char)
else:
    print("Does not start with", char)
