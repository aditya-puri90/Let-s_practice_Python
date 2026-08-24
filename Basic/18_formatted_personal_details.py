'''Personal Details

Take the user's:

Name
Age
City

Print them in this format:

----- Personal Details -----
Name: Aditya
Age: 21
City: Pune
----------------------------

Use \n and \t somewhere in your output.'''

Name = str(input("Enter the users name:"))
Age = int(input("Enter the users age:"))
city = str(input("Enter the users city:"))

print("\n---- Personal Details ----")
print("\t Name :",Name)
print("\t Age :", Age)
print("\t City :", city)
print("---------------")