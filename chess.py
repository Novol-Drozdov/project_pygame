import pygame
pygame.init()

WIDTH, HEIGHT = 400, 400
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cCol, cRow = 4, 4

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: cCol -= 1
            elif event.key == pygame.K_RIGHT: cCol += 1
            elif event.key == pygame.K_UP: cRow -= 1
            elif event.key == pygame.K_DOWN: cRow += 1

            cCol %= 8
            cRow %= 8

    window.fill('black')
    color = 'gray'
    for row in range(8):
        for col in range(8):
            pygame.draw.rect(window, color, (col * 50, row * 50, 50, 50))
            if color == 'gray': color = 'black'
            else: color = 'gray'
        if color == 'gray': color = 'black'
        else: color = 'gray'

    pygame.draw.rect(window, 'blue', (cCol * 50, cRow * 50, 50, 50), 5)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()