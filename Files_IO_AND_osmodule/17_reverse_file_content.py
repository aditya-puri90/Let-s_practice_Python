'''Q17. Reverse File Content

Read a file and write its content in reverse order into another file.
'''

with open("notes.txt", "r") as file:
    content = file.read()
    reversed_content = content[::-1]

with open("Reversed.txt", "w") as f:
    f.write(reversed_content)

print("File content reversed successfully into Reversed.txt!")
