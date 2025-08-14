import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Bullet:
    def __init__(self, posStart, posDirect, speed):
        bullets.append(self)

        self.px, self.py = posStart
        dx, dy = posDirect[0] - posStart[0], posDirect[1] - posStart[1]
        dist = (dx ** 2 + dy ** 2) ** 0.5
        self.sx, self.sy = (dx / dist) * speed, (dy / dist) * speed

    def update(self):
        self.px += self.sx
        self.py += self.sy

        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)

    def draw(self):
        pygame.draw.circle(window, 'black', (self.px, self.py), 2)

bullets = []

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            Bullet((WIDTH // 2, HEIGHT // 2), (mx, my), 10)
    for b in bullets: b.update()

    window.fill('white')
    for b in bullets: b.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
