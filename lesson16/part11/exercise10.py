class Person:
    def __init__(self, full_name, age, id_number):
        self.full_name = full_name
        self.age = age
        self.id_number = id_number


class Account:
    def __init__(self, number, owner, amount):
        self.number = number
        self.owner = owner
        self.amount = amount

    def transfer_to(self, account, amount):
        if amount <= self.amount:
            self.amount -= amount
            account.amount += amount
            print(f"{self.owner.full_name} transfered {amount} to {account.owner.full_name}")
        else:
            print("Not enough credit!")

    def print_account_info(self):
        print(f"Account number: {self.number} \nOwner: {self.owner.full_name} \nAmount: {self.amount} \n")


p1 = Person("Bob Ross", "dead", "123121233")
p2 = Person("Samwise Gangee", 102, "None")

account1 = Account("123456789000000", p1, 8560387560.378)
account2 = Account("987654321000000", p2, 1458)
account1.transfer_to(account2, 560387560.378)

account1.print_account_info()
account2.print_account_info()
