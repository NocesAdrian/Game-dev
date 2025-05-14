import pygame
import sys

screen_height = 600
screen_width = 500

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("src/assets/characters/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.speed = 8

        self.key = pygame.key.get_pressed()

        if self.key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.key[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += self.speed

#
#   ALL EVENTS RUN HERE
#

class GameLoop:
    def __init__(self):
        self.init = pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.title = pygame.display.set_caption("Space Invaders")

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.assets()

        # creates the player
        self.player = Player(int(screen_width / 2), screen_height - 100)
        self.PlayerGroup()

    #
    #   ASSETS
    #

    def assets(self):
        self.src = "src/assets"
        self.bg = pygame.image.load(f"{self.src}/bg/bg.png")

    #
    #   INITIALIZE GROUPS
    #

    def PlayerGroup(self):
        self.playerGroup = pygame.sprite.Group()
        self.playerGroup.add(self.player)

    #
    #   MAIN LOOP
    #

    def run(self):
        self.running = True
        
        # runs the game
        while self.running == True:

            self.clock.tick(self.fps)
            #self.screen.fill((255,255,255))
            self.screen.blit(self.bg, (0, 0))

            # handles events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #updates player position
            self.player.update()

            # draws the player to the screen
            self.playerGroup.draw(self.screen)

            #update entire screen every loop
            self.flip = pygame.display.flip()

        pygame.quit() 
        sys.exit()




#
#   RUN THE GAME
#

if __name__=="__main__":
    game = GameLoop()
    game.run()
