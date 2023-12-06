class Player:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def change_x(self, input):
        self.x = self.x + input

    def change_y(self, input):
        self.y = self.y + input