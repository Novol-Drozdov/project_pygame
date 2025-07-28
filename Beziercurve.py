import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x1, y1 = WIDTH // 4, HEIGHT
x2, y2 = 0, 0
x3, y3 = WIDTH, 0
x4, y4 = WIDTH // 4 * 3, HEIGHT

t = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    # Для двух точек:   P = (1-t) * P1 + t * P2
    # Для трёх точек:   P = (1-t) ** 2 * P1 + 2 * (1-t) * P2 + t ** 2 * P3
    # Для четырёх точек:    P = (1-t)** 3 * P1 + 3 * (1-t) ** 2 * t * P2 + 3 * (1-t) * t ** 2 * P3 + t ** 3 * P4
    
    mx, my = pygame.mouse.get_pos()

    x4, y4 = mx, my

    t += 1 / 300
    if t > 1: t = 0
    x = (1-t)** 3 * x1 + 3 * (1-t) ** 2 * t * x2 + 3 * (1-t) * t ** 2 * x3 + t ** 3 * x4
    y = (1-t)** 3 * y1 + 3 * (1-t) ** 2 * t * y2 + 3 * (1-t) * t ** 2 * y3 + t ** 3 * y4


    window.fill('black')
    for d in range(300):
        dd = d / 300
        dx = (1-dd)** 3 * x1 + 3 * (1-dd) ** 2 * dd * x2 + 3 * (1-dd) * dd ** 2 * x3 + dd ** 3 * x4
        dy = (1-dd)** 3 * y1 + 3 * (1-dd) ** 2 * dd * y2 + 3 * (1-dd) * dd ** 2 * y3 + dd ** 3 * y4
        pygame.draw.circle(window, 'gray20', (dx, dy), 2)


    pygame.draw.rect(window, 'brown', (WIDTH // 2 - 20, HEIGHT // 2, 40, HEIGHT // 2))
    pygame.draw.circle(window, 'blue', (x1, y1), 20)
    pygame.draw.circle(window, 'gray', (x2, y2), 20)
    pygame.draw.circle(window, 'gray20', (x3, y3), 20)
    pygame.draw.circle(window, 'red', (x4, y4), 20)

    pygame.draw.circle(window, 'yellow', (x, y), 10)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
