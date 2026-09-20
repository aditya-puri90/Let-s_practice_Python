'''Q15. Find a Word

Check whether a target word exists in a text file.
'''

word = "Python"

with open("notes.txt", "r") as f:
    content = f.read()

words_in_file = [w.strip(".,!?:;") for w in content.split()]

if word in words_in_file or word.lower() in [w.lower() for w in words_in_file]:
    print(f"Word '{word}' found in file.")
else:
    print(f"Word '{word}' not found in file.")
