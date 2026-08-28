'''Q22. Count Vowels and Consonants

Take a string and count:
- Vowels
- Consonants

Ignore spaces.
'''

text = input("Enter string: ")

count_vowels = 0
count_con = 0

for char in text:
    if char.lower() in "aeiou":
        count_vowels += 1
    elif char.isalpha():
        count_con += 1

print("Vowels:", count_vowels)
print("Consonants:", count_con)
