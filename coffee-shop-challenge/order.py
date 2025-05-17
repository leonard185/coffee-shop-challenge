class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name
        self.orders = []

    @property
    def name(self):
        """Return the customer’s name."""
        return self._name

    @name.setter
    def name(self, value):
        """Enforce type=str and length 1–15."""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1–15 characters long")
        self._name = value

    def __repr__(self):
        return f"<Customer {self.name!r}>"


class Coffee:
    def __init__(self, blend):
        if not isinstance(blend, str):
            raise TypeError("Blend must be a string")
        self.blend = blend
        self.orders = []

    def __repr__(self):
        return f"<Coffee {self.blend!r}>"


class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")

        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        price = float(price)
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
        self._price = price

        self.customer = customer
        self.coffee = coffee
        customer.orders.append(self)
        coffee.orders.append(self)

    @property
    def price(self):
        """Return the order price (immutable)."""
        return self._price

    def __repr__(self):
        return (
            f"<Order {self.customer.name!r} -> {self.coffee.blend!r} "
            f"@ ${self.price:.2f}>"
        )


if __name__ == "__main__":
    alice   = Customer("Alice")
    bob     = Customer("Bob")
    eve     = Customer("Eve")
    mallory = Customer("Mallory")
    trent   = Customer("Trent")

    espresso  = Coffee("Espresso")
    latte     = Coffee("Latte")
    americano = Coffee("Americano")

    examples = [
        Order(alice,   espresso,  2.50),
        Order(bob,     latte,     3.75),
        Order(eve,     americano, 4.25),
        Order(mallory, espresso,  1.99),
        Order(trent,   latte,     5.00),
    ]

    for o in examples:
        print(o)

    print(f"\n{espresso.blend} has {len(espresso.orders)} orders.")
    print(f"{latte.blend} has {len(latte.orders)} orders.")
    print(f"{americano.blend} has {len(americano.orders)} orders.")

    print(f"\n{alice.name} placed {len(alice.orders)} order(s).")
    print(f"{bob.name} placed {len(bob.orders)} order(s).")
