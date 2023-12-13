import pygame 
import os
import re

"""
author @ taylor - base gpt-generated, but built on me. 
purpose: manages game's graphics
"""

class CoffeeShopView:
    def __init__(self, width, height, controller, player):
        pygame.init()

        #set up screen
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.corresponding = {
            "IDLE": self.idle, 
            "GRIND_BEANS": self.grinding_beans, 
            "BREW": self.brewing, 
        }

        #load some images: 
        self.background_image = self.load_image("images/backgrounds/background.png")
        self.cutscreen = self.load_image("images/backgrounds/cutscreen.png")
        self.coffee_grinder = self.load_coffee_grinding_images("images/coffee_grinder")
        self.brewing_images = self.load_brewing_images("images/coffee_machine")

        #some of the objects
        self.controller = controller
        self.player = player
        
        pygame.display.set_caption("Latte Simulator")
        self.clock = pygame.time.Clock()

    #**********render whatever you need to render**********#
    def render(self, state):
        self.corresponding[state]()
        pygame.display.flip()
        self.clock.tick(60)  

    #**********misc helper functions**********#
    def clear_screen(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def draw_text(self, text, x, y, font_size=24, color=(255, 255, 255)):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    #**********for loading assets**********#
    #to help sort loaded images
    def extract_frame_number(self, file_name):
        match = re.search(r'frame_(\d+)_delay', file_name)
        if match:
            return int(match.group(1))
        return 0 

    def load_brewing_images(self, folder_path):
        images = []
        for img_file in sorted(os.listdir(folder_path), key=self.extract_frame_number):
            if img_file.endswith('.png'):
                path = os.path.join(folder_path, img_file)
                images.append(self.load_image(path)) 
        return images

    def load_coffee_grinding_images(self, folder_path):
        images = []
        def extract_number(file_name):
            parts = file_name.split('-')
            number_part = parts[1] if len(parts) > 1 else '0'
            number = int(number_part.split('.')[0])  
            return number
        for img_file in sorted(os.listdir(folder_path), key=extract_number):
            if img_file.endswith('.png'):
                path = os.path.join(folder_path, img_file)
                images.append(self.load_image(path))
        return images

    #**********image loading and drawing helpers**********#
    def load_image(self, path):
        try:
            image = pygame.image.load(path)
            return image
        except pygame.error as e:
            print(f"Error loading image {path}: {e}")
            return None
        
    def draw_image(self, image, x, y):
        if image:
            self.screen.blit(image, (x, y))

    #**********game over / win screen**********#
    def display_game_over_screen(self):
        self.clear_screen()
        self.draw_text("Game Over!", 250, 200)
        self.draw_text("You served: " + str(self.player.cash) + " customer(s)", 200, 260)
        self.draw_text("Your punishment for subpar barista abilities is...", 85, 300)
        self.draw_text("condemnation to a lifetime of ONLY Starbucks drip coffee!!", 75, 330)

    def display_win(self):
        self.clear_screen()
        self.draw_text("You Win!", 250, 200)
        self.draw_text("You served: " + str(self.player.cash) + " customer(s)", 200, 260)
        self.draw_text("Your reward for your superb barista abilities is...", 95, 300)
        self.draw_text("a lifetime of Breville-made coffee, awaiting you every morning!!", 75, 330)

    #**********idle state**********#
    def idle(self):
        self.screen.fill((255, 255, 255))
        self.draw_image(self.background_image, 0, 40)
        self.draw_machine()
        self.draw_tool_bar()
        for customer in self.player.customers:
            self.draw_customer(customer.x, customer.y)
        self.draw_player()

    def draw_machine(self):
        self.draw_image(self.load_image("images/coffee_machine.png"), 250, 400)
        
    def draw_tool_bar(self):
        self.draw_text("Coffees made: " + str(self.player.coffee_count), 10, 10, color=(0, 0, 0))
        self.draw_text("Customer number: " + str(len(self.player.customers)), 160, 10, color=(0, 0, 0))
        self.draw_text("Cash: " + str(self.player.cash), 350, 10, color=(0, 0, 0))

        heart_x = 430
        for i in range(self.player.lives):
            self.draw_image(self.load_image("images/heart.png"), heart_x, -3)
            heart_x += 50

    def draw_customer(self, customer_x, customer_y):
        self.draw_image(self.load_image("images/customers/customer-1.png"), customer_x, customer_y)
        self.draw_image(self.load_image("images/chat.png"), customer_x, customer_y-50)

    def draw_player(self):
        self.draw_image(self.load_image("images/player.png"), self.player.x, self.player.y)

    #**********grinding beans**********#
    def grinding_beans(self):
        self.screen.fill((255, 255, 255))
        self.draw_image(self.load_image("images/backgrounds/basic-background.png"), 0, 50)
        self.grinding_beans_text()
        self.draw_beans()
        self.draw_drag_line()

    def grinding_beans_text(self):
        self.draw_text("Grinding beans", 20, 10, color=(0, 0, 0))
        self.draw_text(str(self.controller.grind_imgs_thru) + "/" + str(self.controller.grind_imgs_threshold) + " beans", 250, 10, color=(0, 0, 0))

    def draw_beans(self):
        self.draw_image(self.coffee_grinder[self.controller.get_current_image()], -50, 70)

    def draw_drag_line(self):
        pygame.draw.line(self.screen, (255, 0, 0), (190, 150), (380, 150))

    #**********brewing**********#
    def brewing(self):
        self.screen.fill((255, 255, 255))
        self.draw_text("brewing coffee", 50, 50, color=(0, 0, 0))
        self.draw_brewing()
        self.brewing_text()

    def brewing_text(self):
        self.draw_text("Brewing!", 20, 10, color=(0, 0, 0))

    def draw_brewing(self):
        self.draw_image(self.brewing_images[self.controller.get_brewing_frame()], 0, 50)