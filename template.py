import pygame
from random import randint
pygame.init()

WiDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WiDTH, HEIGHT))
clock = pygame.time.Clock()

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
