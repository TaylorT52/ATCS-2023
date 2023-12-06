import pygame 
import json

class Graphics:
    def __init__(self, title, width, height, player, machine):
        pygame.init()
        self.player = player
        self.machine = machine
        self.width = width
        self.height = height
        self.MODE = "CAFE"
        self.draw_map = {"CAFE": self.draw_background, "CUT_SCREEN": self.cut_screen}
        self.background_image = "imgs/background.png"
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.Font(None, 36) 
        self.small_font = pygame.font.Font(None, 20) 
        self.clickable_rects = []
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def set_mode(self, mode):
        self.MODE = mode

    def load_image(self, path):
        try:
            image = pygame.image.load(path)
            return image
        except pygame.error as e:
            print(f"Error loading image {path}: {e}")
            return None

    def draw_image(self, image, x, y):
        self.screen.blit(image, (x, y))

    def update_screen(self):
        pygame.display.flip()
        self.clock.tick(60) # 60fps

    def clear_screen(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def draw_screen(self):
        self.draw_map[self.MODE]()

    def draw_player(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.player.x, self.player.y, 50, 50))

    def draw_machine(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.machine.x, self.machine.y, 50, 50))

    def draw_background(self):
        if self.background_image:
            self.screen.blit(self.load_image(self.background_image), (0, 40))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.width, 70))
        self.screen.blit(self.load_image("imgs/coffee_beans.png"), (self.width-90, 7))
        text_surface = self.font.render(str(self.player.coffee_beans), True, (255, 255, 255))
        self.screen.blit(text_surface, (self.width-60, 43))
        self.draw_player()
        self.draw_machine()

    def cut_screen(self):
        self.screen.blit(self.load_image("imgs/cutscreen.png"), (0, 40))
        text_surface = self.font.render('Make a latte', True, (0, 0, 0))
        self.screen.blit(text_surface, (self.width/2-60, 100))
        x_category = 50
        x_item = 60
        y = 140
        padding_x = 5
        padding_y = 5

        with open('selections.json', 'r') as file:
            coffee_menu = json.load(file)

            for category, items in coffee_menu.items():
                text_surface = self.font.render(category, True, (0, 0, 0))
                self.screen.blit(text_surface, (x_category, y))
                y += 35
                for item in items:
                    text_surface = self.small_font.render(f"{item['name']}: {item.get('description', 'No description available')}", True, (0, 0, 0))
                    text_rect = text_surface.get_rect(topleft=(x_item, y))
                    padded_rect = pygame.Rect(text_rect.left - padding_x, text_rect.top - padding_y,
                                      text_rect.width + 2 * padding_x, text_rect.height + 2 * padding_y)
                    pygame.draw.rect(self.screen, (211, 211, 211), padded_rect)
                    self.clickable_rects.append((padded_rect, item))
                    self.screen.blit(text_surface, (x_item, y))
                    y+= 20
                y+= 15

    def draw_outline(self, rect):
        outline_color = (0, 0, 0) 
        outline_thickness = 2 
        pygame.draw.rect(self.screen, outline_color, rect, outline_thickness)
                