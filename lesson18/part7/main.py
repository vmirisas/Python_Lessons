from customer import Customer
from order import Order
from payment import Payment
from credit import Credit
from check import Check


def main():
    customer1 = Customer("John Wick", "Makedonias 3")
    customer1.place_order(Order("20201215", Payment(100000)))
    customer1.place_order(Order("20201216", Payment(250000)))
    customer2 = Customer("Nemo", "MC Wallaby 42")
    customer2.place_order(Order("20201205", Credit(34235, "2349673", "20221010")))
    customer2.place_order(Order("20201205", Credit(5436, "2349673", "20221010")))
    customer3 = Customer("John Snow", "The Wall")
    customer3.place_order(Order("20201203", Payment(4234)))
    customer3.place_order(Order("20203905", Credit(5436, "746853", "20221111")))
    customer3.place_order(Order("20203905", Check(654735, "555555", "20210203")))
    print(customer1)
    print("")
    print(customer2)
    print("")
    print(customer3)


main()
