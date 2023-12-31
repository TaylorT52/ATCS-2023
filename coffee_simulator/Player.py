
"""
author @ taylor
purpose: player obj, keeps track of your stats
"""

class Player:
    def __init__(self, x, y, max_customers):
        #player pos
        self.x = x
        self.y = y

        #num customers you can have before you start losing lives
        self.max_customers = max_customers

        #orders, etc.
        self.coffee_count = 0
        self.customer_count = 0
        self.customers = []
        self.orders = []
        self.cash = 0
        self.lives = 3
 
    #add customers, serve etc. fairly simple
    def add_customer(self, customer, order):
        self.customers.append(customer)
        self.orders.append(order)
        self.customer_count += 1

    #serve customer, make $$$ :D 
    def serve_customer(self):
        self.customer_count -= self.coffee_count
        for i in range(self.coffee_count-1):
            self.customers.pop(0)
            self.cash += 1
        self.coffee_count = 0

    #tracks player's lives; customer leaves if over three there
    def check_player_lives(self):
        if self.customer_count >= self.max_customers: 
            self.lives -= 1
            self.customer_count -= 1
            self.customers.pop()
        