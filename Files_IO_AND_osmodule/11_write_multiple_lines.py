'''Q11. Write Multiple Lines

Create:
subjects.txt

and write multiple lines using writelines().
'''

with open("subjects.txt", "w") as f:
    subjects = ["Python\n", "SQL\n", "Statistics\n", "Machine Learning\n", "Power BI\n"]
    f.writelines(subjects)

print("Subjects written successfully!")
