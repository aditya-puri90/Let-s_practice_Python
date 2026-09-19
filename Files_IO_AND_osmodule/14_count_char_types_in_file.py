'''Q14. Count Character Types in File

Read a file and count:
- Uppercase letters
- Lowercase letters
- Digits
- Spaces
'''

with open("notes.txt", "r") as f:
    content = f.read()

uppercase = 0
lowercase = 0
digits = 0
spaces = 0

for char in content:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
