from payment import Payment


class Check(Payment):
    def __init__(self, amount, number, bank_code):
        super().__init__(amount)
        self.number = number
        self.bank_code = bank_code

    def __str__(self):
        return f"{super().__str__()} Credit Number: {self.number} Bank Code: {self.bank_code}"
