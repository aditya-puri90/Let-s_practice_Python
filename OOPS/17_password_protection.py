'''
Q17. Password protection

Create a User class with:

username
__password

Create a method to verify whether the entered password is correct.
'''

class User:

    def __init__(self,username,_password):
        self.username = username
        self._password = _password

    def verify(self,entered_password):
        if self._password == entered_password:
            return "Access granted"
        else:
            return "Access Denied"

u1 = User("Adityap","azxcbyn")

print(u1.verify("azxcbyn"))
print(u1.verify("mypass"))

print(u1._password)