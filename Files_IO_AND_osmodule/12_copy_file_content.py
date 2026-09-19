'''Q12. Copy File Content

Read the contents of source.txt and write the same content into backup.txt.
'''

# Ensure source file exists with sample content
with open("source.txt", "w") as f:
    f.write("This is the source file containing important data for backup.\n")

with open("source.txt", "r") as source_file:
    content = source_file.read()

with open("backup.txt", "w") as backup_file:
    backup_file.write(content)

print("File copied successfully from source.txt to backup.txt!")
