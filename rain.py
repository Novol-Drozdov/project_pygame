import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Drop:
    def __init__(self):
        self.px, self.py = randint(0, WIDTH), randint(0, HEIGHT)
        self.size = randint(1, 5)
        c = 5 + self.size * 50
        self.color = (c, c, c)

    def update(self):
        self.py += self.size * 2

        if self.py > HEIGHT:
            self.py = randint(-HEIGHT, 0)

    def draw (self):
        pygame.draw.circle(window, self.color, (self.px, self.py), self.size)

rain = []

for _ in range(1000):
    rain.append(Drop())

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    for drop in rain: drop.update()

    window.fill('black')
    for drop in rain: drop.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
