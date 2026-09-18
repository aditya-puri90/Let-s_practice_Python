'''Q8. Count Characters

Read a text file and count the total number of characters.
'''

with open("students.txt", "r") as f:
    content = f.read()
    char_count = len(content)

print("Total number of characters:", char_count)
