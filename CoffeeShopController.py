from CoffeeMachine import CoffeeMachine
from Customer import Customer
import time

class CoffeeShopController:
    def __init__(self, player):
        self.player = player
        self.machine = CoffeeMachine(250, 400)

        #idle
        self.clicked_box = False

        #grinding beans stuff
        self.current_image_index = 0
        self.last_image_index = 0
        self.grind_imgs_thru = 0
        self.grind_imgs_threshold = 200

        #brewing stuff
        self.brewing_frame = 0
        self.brewing_frame_count = 205
        self.keep_brewing = True

    def init_fsm(self):
        self.machine.add_transition("IDLE", self.idle, "GRIND_BEANS")
        self.machine.add_transition("GRIND_BEANS", self.grind_beans, "BREW")
        self.machine.add_transition("BREW", self.brew, "IDLE")
        #self.machine.add_transition("STEAM_MILK", self.steam_milk, "IDLE")

    def handle_click(self, x, y):
        clickable_box = self.machine.get_clickable_box()
        if self.machine.current_state == "IDLE":
            if clickable_box.collidepoint(x, y):
                self.machine.process()
            for customer in self.player.customers:
                if customer.get_customer_rect().collidepoint(x, y):
                    self.player.serve_customer()
                    print("customer served!")

    def handle_mouse_position(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]

        if self.machine.current_state == "GRIND_BEANS":
            start = (190, 150)
            end = (380, 150)
            line_length = end[0] - start[0]

            segment_length = line_length / 13 
            relative_x = x - start[0]
            if 0 <= relative_x <= line_length:
                self.current_image_index = int(relative_x // segment_length)
                if self.current_image_index != self.last_image_index:
                    self.grind_imgs_thru += 1
                    self.last_image_index = self.current_image_index
            else:
                self.current_image_index = 0

    def get_current_image(self):
        return self.current_image_index

    def idle(self):
        pass

    def grind_beans_temp(self):
        print(self.grind_imgs_thru)
        if self.grind_imgs_thru >= self.grind_imgs_threshold: 
            self.grind_imgs_thru = 0 
            self.machine.process()

    def brew_temp(self):
        if self.machine.current_state == "BREW":
            if self.brewing_frame < self.brewing_frame_count-1 and self.keep_brewing:
                self.brewing_frame += 1
                if self.brewing_frame == 0:
                    time.sleep(0.1)
            else:
                self.brewing_frame = 0
                self.keep_brewing = False
                time.sleep(0.5)
                self.machine.process()
                self.keep_brewing = True
                self.player.coffee_count += 1


    def get_brewing_frame(self):
        return self.brewing_frame

    def grind_beans(self):
        pass

    def brew(self):
        pass

    def steam_milk(self):
        pass

    def get_state(self):
        return self.machine.current_state

        