import pygame
import sys
from src.entities.player import Player

#
#   ALL EVENTS RUN HERE
#

class GameLoop:
    def __init__(self, screen_width, screen_height, title, fps):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.init = pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.title = pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.fps = fps

        self.assets()

        # creates the player
        self.player = Player(int(self.screen_width / 2), self.screen_height - 70, 3)
        self.Groups()

    #
    #   ASSETS
    #

    def assets(self):
        self.bg = pygame.image.load("src/assets/bg/bg.png").convert()

    #
    #   INITIALIZE GROUPS
    #

    def Groups(self):
        self.playerGroup = pygame.sprite.Group()
        self.bulletGroup = pygame.sprite.Group()
        self.playerGroup.add(self.player)

    #
    #   MAIN LOOP
    #

    def run(self):
        self.running = True
        
        # runs the game
        while self.running == True:

            self.screen_x, self.screen_y = pygame.display.get_surface().get_size()

            self.clock.tick(self.fps)

            #self.screen.fill((255,255,255))
            
            self.bg_scaled = pygame.transform.scale(self.bg, (self.screen_x, self.screen_y))
            self.screen.blit(self.bg_scaled, (0, 0))

            # handles events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            
            
            #updates player position
            self.player.update(self.screen_x,self.screen_y, self.screen, self.bulletGroup)

            # update bullet group
            self.bulletGroup.update()

            # draws the player to the screen
            self.playerGroup.draw(self.screen)
            self.bulletGroup.draw(self.screen)

            #update entire screen every loop
            self.flip = pygame.display.flip()

        pygame.quit() 
        sys.exit()
