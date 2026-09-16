"""
Q34. Multiple Dunder Methods (__init__, __str__, __eq__)

Create a Book class and implement:
    __init__()
    __str__()
    __eq__()
Compare two books based on their ISBN number.
"""


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = str(isbn)

    def __str__(self):
        return f"Book(Title='{self.title}', Author='{self.author}', ISBN='{self.isbn}')"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False


if __name__ == "__main__":
    b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "12345")
    b2 = Book("1984", "George Orwell", "67890")
    b3 = Book("The Great Gatsby (Special Edition)", "F. Scott Fitzgerald", "12345")

    print("Book 1:", b1)
    print("Book 2:", b2)
    print("Book 3:", b3)

    print("Is Book 1 equal to Book 2?", b1 == b2)
    print("Is Book 1 equal to Book 3?", b1 == b3)
