class Author:
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email


class Book:
    def __init__(self, title, authors, price, copies):
        self.title = title
        self.authors = authors
        self.price = price
        self.copies = copies

    def print_full_title(self):
        authors_names = [author.full_name for author in self.authors]
        print(f" Title: '{self.title}', Authors: {', '.join(authors_names)}")

    def add_author(self, author):
        self.authors.append(author)


p1 = Author("Bob Patterson", "bob@pcookbook.com")
p2 = Author("James McConan", "james@cookbook.com")
b = Book("The Ultimate Python Cook Book", [p1, p2], 18.25, 43)
b.print_full_title()
b.add_author(Author("Tom Rassbow", "tom@cookbook.com"))
b.print_full_title()
