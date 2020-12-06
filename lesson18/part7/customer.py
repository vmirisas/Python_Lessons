
class Customer:
    def __init__(self, full_name, address, orders=None):
        self.full_name = full_name
        self.address = address
        if orders is None:
            self.orders = []
        else:
            self.orders = orders

    def place_order(self, order):
        self.orders += [order]

    def __str__(self):
        sum = 0
        st = f"Customer: {self.full_name}\n"
        st += f"Address: {self.address}\n"
        st += "=" * 20 + "\n"
        st += "ORDERS\n"
        for order in self.orders:
            st += f"{order}\n"
            sum += order.payment.amount
        st += "-" * 35 + "\n"
        st += f"Total: {sum}"
        return st
