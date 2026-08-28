'''Q29. Find the Largest Word ⭐⭐⭐

Take a sentence:
Python is an amazing programming language

Find the longest word.

Expected:
programming

💡 You can use .split().
'''

text = input("Enter string: ")
words = text.split()
largest = ""

for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest word:", largest)
