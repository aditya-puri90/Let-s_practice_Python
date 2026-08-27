'''Q5. Count a Character

Take a string and a character from the user.
Count how many times that character appears.

Example:
Enter string: banana
Enter character: a
Count = 3
'''

string = input("Enter string: ")
char = input("Enter character: ")

count = string.count(char)
print("Count =", count)
