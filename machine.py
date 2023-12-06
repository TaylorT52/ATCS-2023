import pygame 

class CoffeeMachine:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.width = 50
        self.height = 50
        self.state_transitions = {}
        self.current_state = "STABLE"
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def add_transition(self, input_symbol, state, action=None, next_state=None):
        self.state_transitions[(input_symbol, state)] = (action, next_state)

    def get_transition(self, input_symbol, state):
        return self.state_transitions[(input_symbol, state)]

    def process(self, input_symbol):
        action, next = self.get_transition(input_symbol, self.current_state)
        if not action == None: 
            action()

        if not next == None: 
            self.current_state = next

    