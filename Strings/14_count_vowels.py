'''Q14. Count Vowels

Take a string and count how many vowels (a, e, i, o, u) it contains.

Example:
Input: education
Vowels = 5
'''

string = input("Enter a string: ")
count = 0

for char in string:
    if char.lower() in "aeiou":
        count += 1

print("Vowels =", count)
