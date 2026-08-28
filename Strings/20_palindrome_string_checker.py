'''Q20. Palindrome String ⭐

Take a string and check whether it is a palindrome.

Examples:
- madam → Palindrome
- python → Not Palindrome

Try using slicing.
'''

text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
