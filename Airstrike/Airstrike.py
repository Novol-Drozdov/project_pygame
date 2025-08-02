import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

imgAim = pygame.image.load('project_pygame/Airstrike/aim.png').convert_alpha()
imgBomb = pygame.image.load('project_pygame/Airstrike/bomb.png').convert_alpha()

imgBombMini = pygame.transform.scale(imgBomb, (imgBomb.get_width() // 5, imgBomb.get_height() // 5))

liveMax = 10
lives = liveMax

bombs = []
bombSpeed = 5
bombCount = 50
bombTimer = 120

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            
            for i in range(len(bombs)-1, -1, -1):
                bombRect = bombs[i]

                if bombRect.collidepoint(mx, my):
                    bombCount -= 1
                    bombs.pop(i)

    mx, my = pygame.mouse.get_pos()

    if bombTimer > 0: bombTimer -= 1
    else:
        bombTimer = randint(30, 120)
        bomRect = imgBomb.get_rect(midtop=(randint(50, WIDTH - 50), -100))
        bombs.append(bomRect)

    for i in range(len(bombs)-1, -1, -1):
        bombRect = bombs[i]
        bombRect.y += bombSpeed
        
        if bombRect.bottom > HEIGHT:
            lives -= 1
            bombCount -= 1
            
            if lives < 1: play = False
            bombs.pop(i)

    if lives <= 0:
        print('Вы проиграли.')
        play = False
    elif bombCount <= 0:
        print('Вы победили!')
        play = False
    
    window.fill('lightblue')
    for bombRect in bombs:
        window.blit(imgBomb, bombRect)
        
    aimRect = imgAim.get_rect(center=(mx, my))
    window.blit(imgAim, aimRect)

    for i in range(liveMax):
        pygame.draw.rect(window, 'gray70', (10 + i * 8, 10, 6, 20))
        i < lives and pygame.draw.rect(window, 'red', (10 + i * 8, 10, 6, 20))

    for i in range(bombCount):
        window.blit(imgBombMini, (WIDTH - i * 10 - 20, 10))
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
