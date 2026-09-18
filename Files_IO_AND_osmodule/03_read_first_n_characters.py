'''Q3. Read Character by Character

Read a text file using read(n) and print only the first 20 characters.
'''

with open("notes.txt", "r") as f:
    content = f.read(20)
    print("First 20 characters:")
    print(content)
