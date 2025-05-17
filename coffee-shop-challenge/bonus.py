class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    @classmethod
    def most_aficionado(cls, coffee):
        all_orders = coffee.orders()
        if not all_orders:
            return None

        customer_totals = {}
        for order in all_orders:
            customer = order.customer
            customer_totals[customer] = customer_totals.get(customer, 0) + order.price

        return max(customer_totals, key=customer_totals.get)


class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)


class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price


paul = Customer("Paul")
jane = Customer("Jane")
mike = Customer("Mike")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

paul.create_order(latte, 5.0)
paul.create_order(latte, 5.5)
jane.create_order(latte, 6.0)
mike.create_order(latte, 4.0)
mike.create_order(espresso, 4.5)

top_spender = Customer.most_aficionado(latte)
print("Most Aficionado (Latte):", top_spender.name if top_spender else "None")
