'''Q31. Username Generator ⭐⭐⭐⭐

Take:
- First Name
- Last Name
- Birth Year

Generate a username.

For example:
First Name: Aditya
Last Name: Puri
Birth Year: 2005

Username: aditya_puri2005

Use string methods and concatenation.
'''

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
birth_year = input("Enter birth year: ")

username = first_name.lower() + "_" + last_name.lower() + birth_year
print("Username =", username)
