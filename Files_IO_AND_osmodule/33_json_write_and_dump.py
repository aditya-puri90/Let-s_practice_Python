'''Q33. Write and Dump JSON Data

Serialize Python dictionaries and lists into a JSON file using json.dump().
'''

import json

student_profile = {
    "name": "Aditya Puri",
    "course": "Python Data Science",
    "modules_completed": 8,
    "skills": ["Python", "SQL", "Machine Learning", "Git & GitHub"],
    "is_active": True
}

with open("student_profile.json", "w") as f:
    json.dump(student_profile, f, indent=4)

print("student_profile.json created successfully!")
