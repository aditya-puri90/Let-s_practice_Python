'''Q19. File Pointer – tell()

Create a file containing 'Python Programming' and use tell() to display the file pointer position.
'''

with open("sample.txt", "w") as f:
    f.write("Python Programming")

with open("sample.txt", "r") as f:
    text = f.read(6)
    print("Read text:", text)
    position = f.tell()
    print("Current file pointer position:", position)
