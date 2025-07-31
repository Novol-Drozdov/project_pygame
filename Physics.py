import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

px, py = WIDTH // 2, HEIGHT // 2
sx, sy = 0, 0
ax, ay = 0, 0
isStand = False

gravity = 1
resist = 0.97

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: ax = -0.5
    elif keys[pygame.K_RIGHT]: ax = 0.5
    else: ax = 0

    if keys[pygame.K_UP]: ay = -2.1
    elif keys[pygame.K_DOWN]: ay = 0.1
    else: ay = 0

    if keys[pygame.K_SPACE] and isStand: sy -= 20

    px += sx
    py += sy
    sx = (sx + ax) * resist
    sy = (sy + ay + gravity) * resist

    if sx < -5: sx = -5
    elif sx > 5: sx = 5

    if px - 15 < 0: px, sx = 15, 0
    if px + 15 > WIDTH: px, sx = WIDTH - 15, 0

    isStand, resist = False, 0.99
    if py + 15 > HEIGHT:
        py, sy, isStand, resist = HEIGHT - 15, -sy / 2, True, 0.85

    window.fill('black')
    pygame.draw.circle(window, 'yellow', (px, py), 15)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
