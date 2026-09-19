'''Q10. Append Data

Open notes.txt in append mode ('a') and add new content without deleting existing text.
'''

with open("notes.txt", "a") as f:
    f.write("\nI am practicing file handling.")

print("Data appended successfully!")
