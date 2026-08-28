'''Q24. Count Uppercase and Lowercase

Take a string and count:
- Uppercase characters
- Lowercase characters

Example:
Input: PyThOn
Uppercase = 3
Lowercase = 3

💡 Look at .isupper() and .islower().
'''

text = input("Enter string: ")
uppercase = 0
lowercase = 0

for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print("Uppercase =", uppercase)
print("Lowercase =", lowercase)
