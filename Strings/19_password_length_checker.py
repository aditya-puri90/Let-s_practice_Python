'''Q19. Password Length

Take a password and check whether its length is at least 8 characters.
'''

password = input("Enter your password: ")

if len(password) >= 8:
    print("Valid password")
else:
    print("Invalid password")
