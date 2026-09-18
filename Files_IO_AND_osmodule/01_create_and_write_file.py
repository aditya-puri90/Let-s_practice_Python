'''Q1. Create and Write a File

Create a file called 'notes.txt' and write introductory text into it.
'''

with open("notes.txt", "w") as f:
    f.write("Python is easy to learn.\n")
    f.write("I am learning Python for Data Science.\n")

print("File notes.txt created and written successfully.")
