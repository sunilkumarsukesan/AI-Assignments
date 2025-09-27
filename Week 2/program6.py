import datetime

class Book:

     def __init__(self, title, author, publication_year):
         self.title = title
         self.author = author
         self.publication_year = publication_year

     def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.publication_year


book1 = Book("Test", "Tester", 2012)
print(f"Book Age: {book1.get_age()} years")

book2 = Book("AI", "AI engg", 2025)
print(f"Book Age: {book2.get_age()} years")