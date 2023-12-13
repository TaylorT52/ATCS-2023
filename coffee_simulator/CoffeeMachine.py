import pygame

"""
author @ taylor - based off @ms. namaisvayam's FSM (gracias!)
purpose: app; coffee machine's fsm
"""

class CoffeeMachine:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.width = 50
        self.height = 50
        self.state_transitions = {}
        self.current_state = "IDLE"

    #basically exact same as prev FSM, except process takes T/F input on whether it can move on
    def add_transition(self, state, action=None, next_state=None):
        self.state_transitions[(state)] = (action, next_state)

    def get_transition(self, state):
        return self.state_transitions[(state)]

    def process(self, input):
        action, next = self.get_transition(self.current_state)
        
        if not action == None: 
            action()

        if not next == None and input: 
            self.current_state = next

    def get_clickable_box(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    