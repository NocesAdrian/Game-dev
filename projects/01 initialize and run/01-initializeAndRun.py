import pygame
import sys

class MyGame:
    def __init__(self):
        self.height = 400
        self.width = 700

        self.init = pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.title = pygame.display.set_caption("MyGame")

        self.clock = pygame.time.Clock()
        self.fps = 60

    def run(self):
        self.running = True
        
        while self.running == True:

            self.clock.tick(self.fps)
            self.screen.fill((255,255,255))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.flip = pygame.display.flip()

        pygame.quit() 
        sys.exit()

if __name__=="__main__":
    game = MyGame()
    game.run()