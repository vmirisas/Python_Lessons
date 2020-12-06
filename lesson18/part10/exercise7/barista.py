from person import Person


class Barista(Person):
    def __init__(self, full_name, salary):
        super().__init__(full_name, salary)

    def prepare(self, customers):
        print(f"Barista {self.full_name} served {customers} customers")
        self.customers_served += customers
