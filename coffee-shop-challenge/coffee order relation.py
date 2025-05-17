class Customer:
    def __init__(self, name):

        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be 1-15 characters long")
        self._name = name

        self._orders = []

    @property
    def name(self):
        """Return the customer’s name."""
        return self._name

    @property
    def orders(self):
        """Return all Order instances for this customer."""
        return list(self._orders)

    def coffees(self):
        """Return unique Coffee instances this customer has ordered."""
        seen = set()
        unique = []
        for order in self._orders:
            coffee = order.coffee
            if coffee not in seen:
                seen.add(coffee)
                unique.append(coffee)
        return unique

    def __repr__(self):
        return f"<Customer {self.name!r}>"


class Coffee:
    def __init__(self, name):

        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = name
        self._orders = []

    @property
    def name(self):
        """Return the coffee’s name."""
        return self._name

    @property
    def orders(self):
        """Return all Order instances for this coffee."""
        return list(self._orders)

    def customers(self):
        """Return unique Customer instances who have ordered this coffee."""
        seen = set()
        unique = []
        for order in self._orders:
            customer = order.customer
            if customer not in seen:
                seen.add(customer)
                unique.append(customer)
        return unique

    def __repr__(self):
        return f"<Coffee {self.name!r}>"


class Order:
    def __init__(self, customer, coffee, price):
        # Type-check
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        # Price validation
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        price = float(price)
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
        self._price = price

        self._customer = customer
        self._coffee = coffee


        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def customer(self):
        """Return the Customer instance for this order."""
        return self._customer

    @property
    def coffee(self):
        """Return the Coffee instance for this order."""
        return self._coffee

    @property
    def price(self):
        """Return the order price (immutable)."""
        return self._price

    def __repr__(self):
        return (
            f"<Order {self.customer.name!r} -> {self.coffee.name!r} @ ${self.price:.2f}>"
        )


if __name__ == "__main__":

    alice = Customer("Alice")
    bob   = Customer("Bob")
    eve   = Customer("Eve")

    # Create coffees
    espresso = Coffee("Espresso")
    latte    = Coffee("Latte")

    # Create orders
    orders = [
        Order(alice,   espresso, 2.50),
        Order(alice,   latte,    3.75),
        Order(bob,     latte,    4.00),
        Order(eve,     espresso, 2.25),
        Order(eve,     espresso, 3.00),
    ]

    # Check Customer relationships
    print("Customer orders and coffees:")
    for customer in (alice, bob, eve):
        print(f"{customer.name} orders: {customer.orders}")
        print(f"{customer.name} coffees: {[c.name for c in customer.coffees()]}\n")

    # Check Coffee relationships
    print("Coffee orders and customers:")
    for coffee in (espresso, latte):
        print(f"{coffee.name} orders: {coffee.orders}")
        print(f"{coffee.name} customers: {[c.name for c in coffee.customers()]}\n")
