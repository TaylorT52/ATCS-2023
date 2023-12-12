import Order
import pygame

class Customer:
    def __init__(self, name, x, y):
        self.name = name
        self.order = None
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50

    def place_order(self, coffee_type):
        self.order = Order(coffee_type)

    def get_customer_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)