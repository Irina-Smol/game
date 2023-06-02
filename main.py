import pygame
import background as bg
from hero import Hero
from enemy import Enemy

def run():
    pygame.init()

    pygame.display.set_caption('UNDERWATER ADVENTURE')
    window = pygame.display.set_mode((bg.WIDTH, bg.HEIGHT))
    clock = pygame.time.Clock()

    background = bg.Background()
    hero = Hero(window)
    enemy = Enemy(5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        background.update()
        background.render(window)
        enemy.update()
        enemy.draw(window)
        hero.update()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    run()