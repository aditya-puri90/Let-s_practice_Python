"""
Q12. Filter Names

Given:
    names = ["Aditya", "Amit", "Rahul", "Ankit", "Rohan"]
Use filter() to select names whose length is greater than 4.
"""

names = ["Aditya", "Amit", "Rahul", "Ankit", "Rohan"]
long_names = list(filter(lambda x: len(x) > 4, names))

if __name__ == "__main__":
    print("Original names:", names)
    print("Names with length > 4:", long_names)
