import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("src/assets/characters/player.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health
        self.lastShot = pygame.time.get_ticks()
        self.cooldown = 200

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, (self.rect.bottom + 8), self.rect.width, 8))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, (self.rect.bottom + 8), (self.rect.width * (self.health_remaining / self.health_start)), 8))

    def update(self, screen_width,screen_height, screen, bulletGroup):
        self.speed = 8
        self.key = pygame.key.get_pressed()
        self.time_now = pygame.time.get_ticks()

        if self.key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.key[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if self.key[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.key[pygame.K_s] and self.rect.bottom < screen_height:
            self.rect.y += self.speed

        
        #if self.key[pygame.K_SPACE] and self.time_now - self.lastShot > self.cooldown:
        if self.time_now - self.lastShot > self.cooldown:
            self.bullet = Bullet(self.rect.centerx, self.rect.top)
            bulletGroup.add(self.bullet)
            self.lastShot = self.time_now

        self.draw(screen)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("src/assets/characters/bullet.png")
        self.image = pygame.transform.scale(self.image, (8, 8))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 8
