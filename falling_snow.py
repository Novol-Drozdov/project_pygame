import pygame
from random import randint
pygame.init()

info = pygame.display.Info()

WiDTH, HEIGHT = info.current_w, info.current_h
FPS = 60

window = pygame.display.set_mode((WiDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

snow = []
count = 2000
maxSize = 5

for i in range(count):
    x, y = randint(0, WiDTH), randint(0, HEIGHT)
    size = randint(1, maxSize)
    snow.append([x, y, size])

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            play = False
    window.fill(pygame.Color('black'))

    mx, my = pygame.mouse.get_pos()

    for obj in snow:
        x, y, size = obj[0], obj[1], obj[2]
        d = ((mx - x) ** 2 + (my - y) ** 2 ) ** 0.5
        if d < 100:
            obj[0] += (x - mx) * 0.3
            obj[1] += (y - my) * 0.3
        obj[1] += obj[2]
        
        if y > HEIGHT + size:
            obj[0] = randint(0, WiDTH)
            obj[1] = -randint(10, 1000)


    for obj in snow:
        x, y = obj[0], obj[1]
        size = obj[2]
        c = 55 + 200 // maxSize * size
        color = (c, c, c)
        pygame.draw.circle(window, color, (x, y), size)

    pygame.draw.circle(window, pygame.Color('yellow'), (mx, my), 100)


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
