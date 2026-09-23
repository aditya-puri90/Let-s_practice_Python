'''Q34. Read and Load JSON Data

Deserialize JSON file contents back into Python dictionaries using json.load().
'''

import json

with open("student_profile.json", "r") as f:
    data = json.load(f)

print("Parsed JSON Profile:")
print("Name:", data.get("name"))
print("Course:", data.get("course"))
print("Modules Completed:", data.get("modules_completed"))
print("Skills:", ", ".join(data.get("skills", [])))
print("Active Status:", data.get("is_active"))
