class Philosopher:
    def __init__(self, full_name, era, books, school):
        self.full_name = full_name
        self.era = era
        self.books = books
        self.school = school
        self.disputed_books = []


philosoher1 = Philosopher("Plato", "Ancient Greece", ["The Republic", "Phaedon"], "Platonism")
philosoher2 = Philosopher("Baruch Spinoza", "Modern Netherlands", ["Ethics", "Political Treatise"], "Modernism")


print(f"{philosoher1.full_name} lived in {philosoher1.era} and wrote the books:{philosoher1.books}.\nHe is of the {philosoher1.school} school of philosophism")
print(philosoher2.disputed_books)
