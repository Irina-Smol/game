import pygame
import background as bg
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __ini__(self, speed):
        super().__init__()
        #pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('image/fish/piran.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = bg.WIDTH
        self.rect.y = randint(60, 750)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()


    def draw(self, window):
        window.blit(self.image, self.rect)