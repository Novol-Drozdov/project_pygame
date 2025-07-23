import pygame
from random import randint
pygame.init()

WiDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WiDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

class Bullet:
    def __init__(self, x, y, speed):
        self.px, self.py = x, y
        self.speed = speed
        bullets.append(self)

    def update(self):
        global scores
        self.py -= self.speed
        if self.py < 0:
            bullets.remove(self)
        for target in targets:
            if target.rect.collidepoint(self.px, self.py):
                targets.remove(target)
                scores += 1

    def draw(self):
        pygame.draw.circle(window, pygame.Color('yellow'), (self.px, self.py), 2)

class Target:
    def __init__(self):
        self.px, self.py = randint(0, WiDTH - 30), -100
        self.speed = 3
        self.rect = pygame.Rect(self.px, self.py, 30, 30)
        targets.append(self)

    def update(self):
        self.py += self.speed
        self.rect.y = self.py
        if self.rect.top > HEIGHT: 
            targets.remove(self)

    def draw(self):
        pygame.draw.rect(window, pygame.Color('red'), self.rect)

gunPX, gunPY = WiDTH // 2, HEIGHT - 30

bullets = []
targets = []

timer = 60
scores = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    mousePX, mousePY = pygame.mouse.get_pos()
    b1, b2, b3 = pygame.mouse.get_pressed()

    gunPX += (mousePX - gunPX) * 0.1    

    if b1:
        b = Bullet(gunPX, gunPY, 5)

    if timer > 0:
        timer -= 1
    else:
        t = Target()
        timer = randint(10, 30)

    for bullet in bullets:
        bullet.update()
    for target in targets:
        target.update() 

    window.fill((0, 0, 0))
    # вывод пушки
    pygame.draw.circle(window, pygame.Color('gray'), (gunPX, gunPY), 10)
    pygame.draw.line(window, pygame.Color('gray'), (gunPX, gunPY), (gunPX, gunPY - 20), 5)
    # отрисовка мешени
    for target in targets:
        target.draw()
    # вывод пуль
    for bullet in bullets:
        bullet.draw()
    
    text =  font.render('Очки: ' + str(scores), 0, pygame.Color('white'))
    window.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
