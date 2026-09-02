"""
Q15. String Analyzer Function

Create analyze_string(text) returning length, uppercase version, and lowercase version.
"""

def analyze_string(text):
    length = len(text)
    uppercase = text.upper()
    lowercase = text.lower()
    return length, uppercase, lowercase

length, upper, lower = analyze_string("Python")

print("Length:   ", length)
print("Uppercase:", upper)
print("Lowercase:", lower)
