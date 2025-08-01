import pygame
from random import randint
from pathlib import Path
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BASE_DIR = Path(__file__).parent

pygame.display.set_caption('Flappy Bird')

font1 = pygame.font.Font(None, 35)
font2 = pygame.font.Font(None, 8)

icon = pygame.image.load(Path('project_pygame') / 'Flappy_Bird' / 'images' / 'icon.png')
imgBG = pygame.image.load(Path('project_pygame') / 'Flappy_Bird' / 'images' / 'background.png')
imgPT = pygame.image.load(Path('project_pygame') / 'Flappy_Bird' / 'images' / 'pipe_top.png')
imgPB = pygame.image.load(Path('project_pygame') / 'Flappy_Bird' / 'images' / 'pipe_bottom.png')
imgBird = pygame.image.load(Path('project_pygame') / 'Flappy_Bird' / 'images' / 'bird.png')

pygame.display.set_icon(icon)

pygame.mixer.music.load(Path('project_pygame') / 'Flappy_Bird' / 'sounds' / 'music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

sndFall = pygame.mixer.Sound(Path('project_pygame') / 'Flappy_Bird' / 'sounds' / 'fall.wav')

py, sy, ay = HEIGHT // 2, 0, 0
player = pygame.Rect(WIDTH // 3, py, 34, 24)
frame = 0

state = 'start'
timer = 10

pipes = []
bges = []
pipesScores = []

pipeSpeed = 3
pipeGateSize = 200
pipeGatePos = HEIGHT // 2

bges.append(pygame.Rect(0, 0, 288, 600))

lives = 3
scores = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    press = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    click = press[0] or keys[pygame.K_SPACE]

    if timer > 0: timer -= 1

    frame = (frame + 0.2) % 4

    for i in range(len(bges)-1, -1, -1):
        bg = bges[i]
        bg.x -= pipeSpeed // 2

        if bg.right < 0: bges.remove(bg)
        
        if bges[len(bges) - 1].right <= WIDTH:
            bges.append(pygame.Rect(bges[len(bges) - 1].right, 0, 288, 600))

    for i in range(len(pipes)-1, -1, -1):
        pipe = pipes[i]
        pipe.x -= pipeSpeed 

        if pipe.right < 0:
            pipes.remove(pipe)
            if pipe in pipesScores:
                pipesScores.remove(pipe)
        
    if state == 'start':
        
        if click and timer == 0 and len(pipes) == 0: state = 'play'

        py += (HEIGHT // 2 - py) * 0.1
        player.y = py
        
    elif state == 'play':
        if click: ay = -2
        else: ay = 0

        py += sy
        sy = (sy + ay + 1) * 0.98
        player.y = py

        if len(pipes) == 0 or pipes[len(pipes)-1].x < WIDTH - 200:
            pipes.append(pygame.Rect(WIDTH, 0, 50, pipeGatePos - pipeGateSize // 2 ))
            pipes.append(pygame.Rect(WIDTH, pipeGatePos + pipeGateSize // 2 , 52, HEIGHT - pipeGatePos + pipeGateSize))

            pipeGatePos += randint(-100, 100)
            if pipeGatePos < pipeGateSize:
                pipeGatePos = pipeGateSize
            elif pipeGatePos > HEIGHT - pipeGateSize:
                pipeGatePos = HEIGHT - pipeGateSize

        if player.top < 0 or player.bottom > HEIGHT: state = 'fall'

        for pipe in pipes:
            if player.colliderect(pipe): state = 'fall'
            
            if pipe.right < player.left and pipe not in pipesScores:
                pipesScores.append(pipe)
                scores += 5
                pipeSpeed = 3 + scores // 100
        
    elif state == 'fall':
        sndFall.play()
        sy, ay = 0, 0
        pipeGatePos = HEIGHT // 2

        lives -= 1
        if lives > 0:
            state = 'start'
            timer = 60
        else:
            state = 'game over'
            timer = 180
    
    else:
        py += sy
        sy = (sy + ay + 1) * 0.98
        player.y = py

        if timer == 0: play = False

#отрисовка игры
    for bg in bges: window.blit(imgBG, bg)

    for pipe in pipes:
            if pipe.y == 0:
                rect = imgPT.get_rect(bottomleft = pipe.bottomleft)
                window.blit(imgPT, rect)
            else:
                rect = imgPB.get_rect(topleft = pipe.topleft)
                window.blit(imgPB, rect)
    
    image = imgBird.subsurface(34 * int(frame), 0, 34, 24)
    image = pygame.transform.rotate(image, -sy * 2)
    window.blit(image, player)

    text = font1.render('Очки: ' + str(scores), 0, 'black')
    window.blit(text, (10, 10))

    text = font1.render('Жизни: ' + str(lives), 0, 'black')
    window.blit(text, (10, HEIGHT - 30))
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
