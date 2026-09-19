'''Q13. Count Vowels in a File

Read a text file and count the number of vowels (a, e, i, o, u) present in the file.
'''

with open("notes.txt", "r") as file:
    content = file.read().lower()

vowels = "aeiou"
vowel_count = {v: 0 for v in vowels}

for char in content:
    if char in vowels:
        vowel_count[char] += 1

for v, count in vowel_count.items():
    print(f"{v}: {count}")

print("Total vowels:", sum(vowel_count.values()))
