class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = name
        self.orders = []

    @property
    def name(self):
        """Return the coffee’s name."""
        return self._name

    def __repr__(self):
        return f"<Coffee {self.name!r}>"


class Customer:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"<Customer {self.name!r}>"


class Order:
    def __init__(self, customer, coffee):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        self.customer = customer
        self.coffee = coffee
        coffee.orders.append(self)

    def __repr__(self):
        return f"<Order {self.customer.name!r} -> {self.coffee.name!r}>"


if __name__ == "__main__":
    cappuccino = Coffee("Cappuccino")

    alice = Customer("Alice")
    bob   = Customer("Bob")
    eve   = Customer("Eve")
    tom   = Customer("Tom")
    ana   = Customer("Ana")

    examples = [
        Order(alice,   cappuccino),
        Order(bob,     cappuccino),
        Order(eve,     cappuccino),
        Order(tom,     cappuccino),
        Order(ana,     cappuccino),
    ]

    print(f"{cappuccino.name!r} has {len(cappuccino.orders)} orders:")
    for order in cappuccino.orders:
        print(" -", order)


