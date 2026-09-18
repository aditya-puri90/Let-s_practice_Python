'''Q2. Read a File

Read notes.txt and print its complete contents.
'''

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
