import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

targets = []
timer = 120
lives = 10
scores = 0

def aim_draw():
    #отрисовка прицела
    pygame.draw.circle(window, 'white', (mx, my), 1)
    pygame.draw.circle(window, 'white', (mx, my), 20, 1)
    pygame.draw.line(window, 'white', (mx - 25, my), (mx - 15, my))
    pygame.draw.line(window, 'white', (mx + 25, my), (mx + 15, my))
    pygame.draw.line(window, 'white', (mx, my - 25), (mx, my - 15))
    pygame.draw.line(window, 'white', (mx, my + 25), (mx, my + 15))

def lives_draw():
    #отрисовка жизни
    for i in range(10):
        pygame.draw.rect(window, 'gray20', (10 + i * 8, 10, 6, 20))
        pygame.draw.rect(window, 'gray40', (10 + i * 8, 10, 6, 20), 2)

        if i < lives:
            pygame.draw.rect(window, 'red', (10 + i * 8, 10, 6, 20))
            pygame.draw.rect(window, 'orange', (10 + i * 8, 10, 6, 20), 2)



play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    mx, my = pygame.mouse.get_pos()
    mb1, mb2, mb3 = pygame.mouse.get_pressed()

    if timer > 0 : timer -= 1
    else:
        timer = randint(30, 120)
        px, py = randint(50, WIDTH - 50), -50
        raduis = randint(15, 30)
        speed = randint(1, 3)
        targets.append([px, py, raduis, speed])

    
    for i in range(len(targets)-1, -1, -1):
        t = targets[i]
        t[1] += t[3]

        if t[1] + t[2] > HEIGHT:
            lives -= 1
            if lives < 1: play = False
            targets.pop(i)
        if mb1 and (t[0] - mx) ** 2 + (t[1] - my) ** 2 < t[2] ** 2 :
            scores += 1
            targets.pop(i)
            print(scores)

    #отрисовка
    window.fill('black')

    for t in targets:
        pygame.draw.circle(window, 'red', (t[0], t[1]), t[2])

    aim_draw()
    lives_draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
