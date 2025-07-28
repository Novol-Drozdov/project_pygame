import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cellsize = 10
world = []
worldWidth, worldHeight = WIDTH // cellsize, HEIGHT // cellsize


for row in range(worldHeight):
    line = []
    for col in range(worldWidth):
        line.append(0)
    world.append(line)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            file = open('map.txt', 'w')

            for row in range(worldHeight):
                for col in range(worldWidth):
                    file.write(str(world[row][col]))

            file.close()
            print("Карта сохранена!")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            try:
                file = open('map.txt', 'r')

                row, col = 0, 0
                for line in file:
                    for s in line:
                        world[row][col] = int(s)
                        col += 1
                        if col >= worldWidth:
                            row += 1
                            col = 0
            except:
                print("Файл карты не найден!")
                file.close()

    mousePX, mousePY = pygame.mouse.get_pos()
    b1, b2, b3 = pygame.mouse.get_pressed()

    mouseRow, mouseCol = mousePY // cellsize, mousePX// cellsize

    if b1:
        world[mouseRow][mouseCol] = 1
    elif b3:
        world[mouseRow][mouseCol] = 0
    
    window.fill((0,0,0))
    for row in range(worldHeight):
        for col in range(worldWidth):
            x, y = col * cellsize, row * cellsize

            if world[row][col] == 1:
                pygame.draw.rect(window, pygame.Color('gray'), (x, y, cellsize, cellsize))
            else:
                pygame.draw.rect(window, pygame.Color('gray'), (x, y, cellsize, cellsize), 1)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
