from person import Person


class Waiter(Person):
    def __init__(self, full_name, salary):
        super().__init__(full_name, salary)

    def serve(self, customers, barista):
        self.customers_served += customers
        print(f"Waiter {self.full_name} serves {customers} customers")
        barista.prepare(customers)
