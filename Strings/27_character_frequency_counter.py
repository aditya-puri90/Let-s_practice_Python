'''Q27. Character Frequency ⭐⭐⭐

Take a string and a character.

Count how many times the character occurs without using .count().

Example:
String: programming
Character: m
Frequency = 2
'''

text = input("Enter string: ")
character = input("Enter character to count: ")
count = 0

for char in text:
    if char == character:
        count += 1

print("Frequency =", count)
