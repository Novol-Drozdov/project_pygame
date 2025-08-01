import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

world = ['BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
         'B                              B',
         'B                              B',
         'B                              B',
         'B                              B',
         'B       P                      B',
         'B      P                       B',
         'B     P                        B',
         'B  PPP                         B',
         'B                              B',
         'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',]

tileSize = 100
worldPX, worldPY = 0, 0
scrollSpeed = 10
scrollLimitX = -len(world[0]) * tileSize + WIDTH
scrollLimitY = -len(world) * tileSize + HEIGHT

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: worldPX += scrollSpeed
    elif keys[pygame.K_RIGHT]: worldPX -= scrollSpeed
    if keys[pygame.K_UP]: worldPY += scrollSpeed
    elif keys[pygame.K_DOWN]: worldPY -= scrollSpeed

    worldPX = min(max(worldPX, scrollLimitX), 0)
    worldPY = min(max(worldPY, scrollLimitY), 0)


    window.fill('black')
    for row in range(len(world)):
        for col in range(len(world[row])):
            x = worldPX + col * tileSize
            y = worldPY + row * tileSize
            
            if world[row][col] == "B":
                pygame.draw.rect(window, 'green', (x, y, tileSize, tileSize))
            if world[row][col] == "P":
                pygame.draw.rect(window, 'blue', (x, y, tileSize, tileSize))

            pygame.draw.rect(window, 'gray10', (x, y, tileSize, tileSize), 1)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
