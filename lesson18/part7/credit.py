from payment import Payment


class Credit(Payment):
    def __init__(self, amount, number, exp_date):
        super().__init__(amount)
        self.number = number
        self.exp_date = exp_date

    def __str__(self):
        return f"{super().__str__()} Credit Number: {self.number} Exp.Date: {self.exp_date}"
