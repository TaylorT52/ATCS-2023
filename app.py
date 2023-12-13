import pygame
import time
from CoffeeShopController import CoffeeShopController
from CoffeeShopView import CoffeeShopView
from Player import Player
from Customer import Customer

"""
author @ taylor - base gpt-generated, but built on me. 
purpose: app; runs game w/ pygame. manages end-game logic, listens for user input.
"""

class App:
    def __init__(self):
        #game vars
        self.WIDTH = 600
        self.HEIGHT = 700
        self.customer_x = 350
        self.customer_y = 550
        self.GAMEOVER = False
        self.WIN = False
        self.running = True
        self.PLAYER_TO_WIN = 2
        self.spawn_rate = 10000
        #objetcts
        self.player = Player(10, 10)
        self.controller = CoffeeShopController(self.player)
        self.graphics = CoffeeShopView(self.WIDTH, self.HEIGHT, self.controller, self.player)
        #init stuff, timers... 
        self.controller.init_fsm()
        self.SPAWN_CUSTOMER_EVENT = pygame.USEREVENT + 1
        self.controller.handle_music(pygame.mixer)
        pygame.mixer.init()
        pygame.time.set_timer(self.SPAWN_CUSTOMER_EVENT, self.spawn_rate) 
    
    #**********handle events**********#
    def handle_mouse_click(self, event):
        self.controller.handle_click(event.pos[0], event.pos[1])

    #made to spawn customers to serve
    def spawn_customer(self):
        new_customer_name = "Customer"  
        new_customer = Customer(new_customer_name, self.customer_x, self.customer_y)
        self.customer_x += 50
        self.customer_y -= 20
        self.player.add_customer(new_customer, "latte")

    #**********wrapping up game**********#
    def check_end_game(self):
        if self.player.lives <= 0:
            self.GAMEOVER = True
        if self.player.cash >= self.PLAYER_TO_WIN:
            self.WIN = True

        if self.GAMEOVER or self.WIN:
            self.end()
     
    def end(self):
        self.graphics.clear_screen()
        if self.GAMEOVER:
            self.graphics.display_game_over_screen()
        elif self.WIN: 
            self.graphics.display_win()
        self.running = False

        #stop everything
        pygame.display.flip()
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
        time.sleep(50) 

    #**********main loop**********#
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(event)
                elif event.type == self.SPAWN_CUSTOMER_EVENT:
                    self.spawn_customer()
            self.controller.handle_mouse_position(pygame.mouse.get_pos())

            #checks
            self.check_end_game()
            if not self.running:
                break

            self.player.check_player_lives()

            #update FSM
            self.controller.update()
            machine_state = self.controller.get_state()

            #graphics
            self.graphics.render(machine_state)
            
        pygame.quit()


app = App()
app.run()
