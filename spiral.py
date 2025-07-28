import pygame
pygame.init()

WIDTH, HEIGHT = 600, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cellWidth, cellHeight = 50, 50
countCol, countRow = WIDTH // cellWidth, HEIGHT // cellHeight
posCol, posRow = countCol // 2, countRow // 2

direct, countStep, currentStep = 0, 1, 0
timer, timerSpeed = 30, 30

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    if timer > 0: timer -= 1
    else:
        timer = timerSpeed
        if direct == 0: posRow -= 1
        elif direct == 1: posCol -= 1
        elif direct == 2: posRow += 1
        elif direct == 3: posCol += 1

        currentStep += 1
        if currentStep == countStep:
            if direct == 1 or direct == 3: countStep += 1
            direct = (direct  + 1) % 4
            currentStep = 0

    for r in range(countRow):
        for c in range(countCol):
            pygame.draw.rect(window, 'gray20', (c * cellWidth, r * cellHeight, cellWidth, cellHeight), 1)

    pygame.draw.rect(window, 'yellow', (posCol * cellWidth, posRow * cellHeight, cellWidth, cellHeight))


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
