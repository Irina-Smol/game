import pygame

WIDTH = 1200
HEIGHT = 800

class Background():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('image/background/bg.jpg'), (2048, HEIGHT))
        self.rect = self.image.get_rect()
        self.moving_speed = 3
        self.bgX1 = 0
        self.bgY1 = 0
        self.bgX2 = self.rect.width
        self.bgY2 = 0

    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed

        if self.bgX1 <= - self.rect.width:
            self.bgX1 = self.rect.width

        if self.bgX2 <= - self.rect.width:
            self.bgX2 = self.rect.width



    def render(self, window):
        window.blit(self.image, (self.bgX1, self.bgY1))
        window.blit(self.image, (self.bgX2, self.bgY2))
