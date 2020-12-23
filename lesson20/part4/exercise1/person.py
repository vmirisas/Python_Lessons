class Person:
    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary
        self.customers_served = 0

    def report(self):
        print(f"{self.full_name} served {self.customers_served} customers at the end of the day")
