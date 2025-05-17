class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))


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



# Customers
paul = Customer("Paul")
jane = Customer("Jane")
mike = Customer("Mike")
susan = Customer("Susan")
ali = Customer("Ali")

# Coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")
mocha = Coffee("Mocha")
americano = Coffee("Americano")

# Orders
paul.create_order(latte, 4.5)
paul.create_order(espresso, 3.0)
jane.create_order(latte, 5.0)
mike.create_order(mocha, 4.0)
susan.create_order(cappuccino, 4.5)
ali.create_order(espresso, 3.5)
jane.create_order(mocha, 4.2)
mike.create_order(latte, 4.8)
susan.create_order(latte, 5.2)

# --- Print Results ---
print("Latte Orders:", latte.num_orders())  # Should be 4
print("Latte Average Price:", round(latte.average_price(), 2))  # Average of 4.5, 5.0, 4.8, 5.2

print("\nPaul's Coffees:", [c.name for c in paul.coffees()])
print("Jane's Coffees:", [c.name for c in jane.coffees()])
print("Espresso Customers:", [c.name for c in espresso.customers()])
