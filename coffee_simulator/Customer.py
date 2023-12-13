import pygame

"""
author @ taylor 
purpose: keeps track of customer location, can get rect for clicking
"""

class Customer:
    def __init__(self, name, x, y):
        self.name = name
        self.order = None
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50

    def get_customer_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)