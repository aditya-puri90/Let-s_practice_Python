'''Q30. Word Counter ⭐⭐⭐

Take a sentence and count the number of words.

Example:
Input: Python is very easy to learn
Words = 6

Use .split().
'''

text = input("Enter string: ")

words = text.split()
print("Number of words =", len(words))
