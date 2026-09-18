'''Q9. Count Words

Read a text file and count the total number of words.
'''

with open("students.txt", "r") as f:
    content = f.read()
    words = content.split()

word_count = len(words)
print("Total words:", word_count)
