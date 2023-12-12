from CoffeeShopController import CoffeeShopController
from CoffeeShopView import CoffeeShopView
from Player import Player
from Customer import Customer
import pygame

class App:
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 700
        self.customer_x = 350
        self.customer_y = 550
        self.player = Player(10, 10)
        self.controller = CoffeeShopController(self.player)
        self.controller.init_fsm()
        self.graphics = CoffeeShopView(self.WIDTH, self.HEIGHT, self.controller, self.player)
        self.running = True
        self.SPAWN_CUSTOMER_EVENT = pygame.USEREVENT + 1
        self.spawn_rate = 10000
        pygame.time.set_timer(self.SPAWN_CUSTOMER_EVENT, self.spawn_rate) 

    #handle events
    def handle_mouse_click(self, event):
        self.controller.handle_click(event.pos[0], event.pos[1])

    def spawn_customer(self):
        new_customer_name = "Customer"  
        new_customer = Customer(new_customer_name, self.customer_x, self.customer_y)
        self.customer_x += 50
        self.customer_y -= 20
        self.player.add_customer(new_customer, "latte")
        print("customer spawned")

    #main loop
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
            self.controller.grind_beans_temp()
            self.controller.brew_temp()

            machine_state = self.controller.get_state()
            self.graphics.render(machine_state)
            
        pygame.quit()


app = App()
app.run()
