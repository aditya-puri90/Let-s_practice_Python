'''Q20. File Pointer – seek()

Read a file, inspect pointer, and use seek(0) to move the pointer back to the beginning.
'''

with open("notes.txt", "w") as f:
    f.write("Python Programming")

with open("notes.txt", "r") as f:
    text = f.read(6)
    print("First read:", text)
    print("Pointer after first read:", f.tell())

    f.seek(0)
    text_again = f.read()
    print("Second read after seek(0):", text_again)
