

class Order:
    def __init__(self, date, payment):
        self.date = date
        self.payment = payment

    def __str__(self):
        return f"Date: {self.date}, Payment: {self.payment}"
