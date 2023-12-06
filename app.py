from graphics import Graphics
from player import Player
from machine import CoffeeMachine
import pygame

class Game:
    def __init__(self):
        WIDTH = 600
        HEIGHT =  700
        title = "Latte Simulator"
        self.player = Player(0, 0)
        self.coffee_machine = CoffeeMachine(85, 300)
        self.graphics = Graphics(title, WIDTH, HEIGHT, self.player, self.coffee_machine)
        self.player_speed = 10

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.coffee_machine.get_rect().collidepoint(event.pos):
                        self.graphics.set_mode("CUT_SCREEN")

                    pos = event.pos
                    for rect, name in self.graphics.clickable_rects:
                        if rect.collidepoint(pos):
                            print(f"Clicked on: {name}")

                mouse_pos = pygame.mouse.get_pos()
                for rect, name in self.graphics.clickable_rects:
                    if rect.collidepoint(mouse_pos):
                        self.graphics.draw_outline(rect)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_d]:
                    self.player.change_x(self.player_speed)
                if keys[pygame.K_a]:
                    self.player.change_x(-self.player_speed)
                if keys[pygame.K_w]:
                    self.player.change_y(-self.player_speed)
                if keys[pygame.K_s]:
                    self.player.change_y(self.player_speed)

            #graphics
            self.graphics.clear_screen()       
            self.graphics.draw_screen()       
            self.graphics.update_screen()      
           
        pygame.quit()

if __name__=="__main__":
    mygame = Game()
    mygame.run()