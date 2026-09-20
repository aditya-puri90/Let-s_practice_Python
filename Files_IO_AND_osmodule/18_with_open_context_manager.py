'''Q18. Use with open() Context Manager

Demonstrate automatic file closing using the 'with' context manager.
'''

with open("notes.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Total words in file:", len(words))

print("Is file closed outside with block?", file.closed)
