from CoffeeMachine import CoffeeMachine
from Customer import Customer
import time
import pygame

"""
author @ taylor - base gpt-generated, but built on me. 
purpose: controls coffee machine logic. uses FSM in coffee machine
"""

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

    #init the fsm
    def init_fsm(self):
        self.machine.add_transition(("IDLE"), self.idle, "GRIND_BEANS")
        self.machine.add_transition(("GRIND_BEANS"), self.grind_beans, "BREW")
        self.machine.add_transition(("BREW"), self.brew, "IDLE")

    #**********music**********#
    def handle_music(self, mixer):
        self.load_and_play_music(mixer, "music/background-sounds.mp3")

    def load_and_play_music(self, mixer, music_path):
        try:
            mixer.music.load(music_path)
            mixer.music.play(-1) 
        except pygame.error as e:
            print(f"Error loading or playing music: {e}")

    #**********handle events**********#

    #mainly for transition from idle to grinding beans
    def handle_click(self, x, y):
        clickable_box = self.machine.get_clickable_box()
        if self.machine.current_state == "IDLE":
            if clickable_box.collidepoint(x, y):
                self.clicked_box = True
            for customer in self.player.customers:
                if customer.get_customer_rect().collidepoint(x, y):
                    self.player.serve_customer()
                    print("customer served!")

    #mainly for grinding beans - helps move the grinder according to mouse position
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
                if self.current_image_index != self.last_image_index and (self.last_image_index < self.current_image_index):
                    self.last_image_index = self.current_image_index
            else:
                self.current_image_index = 0

    
    #**********FSM methods**********#
    def get_current_image(self):
        return self.current_image_index

    #update the FSM 
    def update(self):
        if self.machine.current_state == "IDLE":
            self.machine.process(self.can_continue_idle())
        elif self.machine.current_state == "GRIND_BEANS":
            self.machine.process(self.can_continue_grind())
        elif self.machine.current_state == "BREW":
            self.machine.process(self.can_continue_brew())

    #idle doesn't do much - it just idles ;) 
    def idle(self):
        pass

    #grinding beans
    def grind_beans(self):
        if self.current_image_index != self.last_image_index:
            print(self.grind_imgs_thru)
            self.grind_imgs_thru += 1
            self.last_image_index = self.current_image_index

    #brewing
    def get_brewing_frame(self):
        return self.brewing_frame
    
    #keep brewing until go thru entire anation
    def brew(self):
         if self.machine.current_state == "BREW":
            if self.brewing_frame < self.brewing_frame_count-1 and self.keep_brewing:
                self.brewing_frame += 1
                if self.brewing_frame == 0:
                    time.sleep(0.1)
            else:
                self.brewing_frame = 0
                self.keep_brewing = False
                time.sleep(0.5)
                self.player.coffee_count += 1
                self.reset()

    #**********checks by state for whether the FSM can move on**********#
    def can_continue_idle(self):
        return self.clicked_box
    
    def can_continue_grind(self):
        if self.grind_imgs_thru >= self.grind_imgs_threshold:
            self.keep_brewing = True
            time.sleep(1)
        return self.grind_imgs_thru >= self.grind_imgs_threshold 
    
    def can_continue_brew(self):
        return not self.keep_brewing

    #**********reset**********#
    def reset(self): 
        self.clicked_box = False
        self.grind_imgs_thru = 0

    def get_state(self):
        return self.machine.current_state

    
    

        