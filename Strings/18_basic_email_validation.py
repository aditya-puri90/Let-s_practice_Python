'''Q18. Email Validation — Basic

Take an email address and check whether it contains:
- @
- .

For now, don't build a full professional email validator.

Example:
Input: aditya@gmail.com
Valid format
'''

email = input("Enter your email: ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Not valid")
