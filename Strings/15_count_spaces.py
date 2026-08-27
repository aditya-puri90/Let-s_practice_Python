'''Q15. Count Spaces

Take a sentence and count how many space characters it contains.

Example:
Input: Python is fun to learn
Spaces = 4
'''

text = input("Enter a sentence: ")

count = 0
for char in text:
    if char == " ":
        count += 1

print("Spaces =", count)
