import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

targetPX, targetPY = 0, 0
timer = 0
scores = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            dist = ( (mx - targetPX) ** 2 + (my - targetPY) ** 2) ** 0.5

            if dist < 20: scores += 20

            timer = 0

    if timer > 0: timer -= 1
    else: 
        timer = 120
        targetPX, targetPY = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        scores -= 10
    
    if scores < - WIDTH // 2:
        print('You lose :(')
    if scores > WIDTH // 2: 
        print('You win :)')

    window.fill('white')
    pygame.draw.rect(window, 'black', (WIDTH // 2 + scores, 0, WIDTH - (WIDTH // 2 + scores), HEIGHT) )
    pygame.draw.circle(window, 'red', (targetPX, targetPY), 20)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
