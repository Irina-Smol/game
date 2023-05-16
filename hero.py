import pygame

class Hero:
    def __init__(self, window):
        self.window = window
        self.image = pygame.transform.scale(pygame.image.load('image/hero/m9.png').convert_alpha(), (300, 300))
        self.rect = self.image.get_rect(center=(600, 400))
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_UP] and self.rect.y > 60:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 650:
            self.rect.y += self.speed


        self.window.blit(self.image, self.rect)
