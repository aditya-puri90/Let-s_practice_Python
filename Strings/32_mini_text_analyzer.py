'''Q32. Mini Text Analyzer ⭐⭐⭐⭐⭐

Take a paragraph from the user and calculate:
- Total characters
- Total words
- Total vowels
- Total consonants
- Total digits
- Total spaces
- Uppercase characters
- Lowercase characters

This combines string traversal, categorization methods, and basic counting logic.
'''

paragraph = input("Enter paragraph: ")

total_characters = len(paragraph)
total_words = len(paragraph.split())

vowels = 0
consonants = 0
digits = 0
spaces = 0
uppercase = 0
lowercase = 0

for char in paragraph:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1

    if char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print("\n====== TEXT ANALYZER ======")
print("Total Characters =", total_characters)
print("Total Words      =", total_words)
print("Vowels           =", vowels)
print("Consonants       =", consonants)
print("Digits           =", digits)
print("Spaces           =", spaces)
print("Uppercase        =", uppercase)
print("Lowercase        =", lowercase)
print("============================")
