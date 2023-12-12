class Player:
    def __init__(self, x, y):
        self.coffee_count = 0
        self.customer_count = 0
        self.customers = []
        self.orders = []

    def add_customer(self, customer, order):
        self.customers.append(customer)
        self.orders.append(order)
        self.customer_count += 1

    def serve_customer(self):
        self.customer_count -= self.coffee_count
        for i in range(self.coffee_count):
            self.customers.pop(0)
        self.coffee_count = 0