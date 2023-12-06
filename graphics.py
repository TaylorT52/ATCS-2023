import pygame 

class Graphics:
    def __init__(self, title, width, height):
        pygame.init()
        self.MODE = "CAFE"
        self.draw_map = {"CAFE": self.draw_background, "CUT_SCREEN": self.cut_screen}
        self.background_image = "imgs/background.png"
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.Font(None, 36) 
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

    def draw_player(self, player):
        pygame.draw.rect(self.screen, (0, 0, 0), (player.x, player.y, 50, 50))

    def draw_machine(self, machine):
        pygame.draw.rect(self.screen, (0, 0, 0), (machine.x, machine.y, 50, 50))

    def draw_background(self):
        if self.background_image:
            self.screen.blit(self.load_image(self.background_image), (0, 40))

    def cut_screen(self):
        self.screen.fill((0, 0, 0))
        text_background = (0, 0, 0) 
        text_surface = self.font.render('Hello, Pygame!', True, (255, 255, 255), text_background)
        self.screen.blit(text_surface, (50, 50))