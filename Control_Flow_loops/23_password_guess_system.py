'''Q23. Password System

Set a password in the program.
Keep asking the user for the password until they enter the correct one.'''

password = "python123"
user_password = input("Enter password: ")

while user_password != password:
    print("Wrong password! Try again.")
    user_password = input("Enter password: ")

print("Correct password!")
