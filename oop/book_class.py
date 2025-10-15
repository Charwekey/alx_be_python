# book_class.py

class Book:
    # Constructor - called automatically when you create a new object
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor - called automatically when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

    # String Representation - user-friendly string (used with print())
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official Representation - developer-friendly, can recreate the object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
