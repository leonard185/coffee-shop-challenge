class Customer:
    def __init__(self, name):
    
        self._name = None
        self.name = name

    @property
    def name(self):
        """Return the customer’s name."""
        return self._name

    @name.setter
    def name(self, value):
        """Enforce type=str and length 1-15 (ASCII only)."""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1-15 characters long")
        self._name = value


class Coffee:
    def __init__(self, blend):
        self.blend = blend
        self.orders = []

    def __repr__(self):
        return f"<Coffee {self.blend!r}>"


class Order:
    def __init__(self, customer, coffee):
        self.customer = customer
        self.coffee = coffee
        coffee.orders.append(self)

    def __repr__(self):
        return f"<Order {self.customer.name!r} -> {self.coffee.blend!r}>"



if __name__ == "__main__":
    
    alice = Customer("Alice")
    print(alice.name)  

    alice.name = "Bob"
    print(alice.name)   

    try:
        alice.name = "" 
    except ValueError as e:
        print("Error:", e)
 

    cafe = Coffee("Cafe Latte")
    order1 = Order(alice, cafe)
    order2 = Order(Customer("Eve"), cafe)
    order3 = Order(Customer("Mallory"), cafe)

    print(f"{cafe.blend} has {len(cafe.orders)} orders:")
    for o in cafe.orders:
        print("-", o)


