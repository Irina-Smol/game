import pygame
from hero import Hero

pygame.init()

pygame.display.set_caption('UNDERWATER ADVENTURE')
window = pygame.display.set_mode((1800, 1000))
clock = pygame.time.Clock()
window.fill((29, 12, 232))
background = pygame.transform.scale(pygame.image.load('image/background/bg.jpg'), (1800, 1000))
hero = Hero(window)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.blit(background, (0, 0))
    hero.update()
    pygame.display.update()
    clock.tick(60)