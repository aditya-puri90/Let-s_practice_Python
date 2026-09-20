'''Q16. Replace a Word

Read a file and replace 'Python' with 'Python Programming'.
Save the modified content back to the file.
'''

with open("notes.txt", "r") as file:
    content = file.read()

modified_content = content.replace("Python", "Python Programming")

with open("notes.txt", "w") as file:
    file.write(modified_content)

print("Replacement done successfully!")
