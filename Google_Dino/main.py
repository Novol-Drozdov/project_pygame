import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 400
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

imgSprites = pygame.image.load('project_pygame/Google_Dino/sprites.png').convert_alpha()
imgBG = imgSprites.subsurface(2, 104, 2400, 26)
imgDinoStand = [imgSprites.subsurface(1514, 2, 88, 94),
                imgSprites.subsurface(1602, 2, 88, 94)]
imgDinoSit = [imgSprites.subsurface(1866, 36, 118, 60),
              imgSprites.subsurface(1984, 36, 118, 60)]
imgDinoLose = [imgSprites.subsurface(1690, 2, 88, 94)]

py, sy = 380, 0
isStand = False
speed = 200
frame = 0

bgs = [pygame.Rect(0, HEIGHT - 50, 2400, 26)]

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    b1, b2, b3 = pygame.mouse.get_pressed()
    pressJump = keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP] or b1
    pressSit = keys[pygame.K_LCTRL] or keys[pygame.K_s] or keys[pygame.K_DOWN] or b3

    if pressJump and isStand: sy = -22
    if isStand: frame = (frame + speed / 35) % 2

    py += sy
    sy = (sy + 1) * 0.97

    isStand = False
    if py > HEIGHT - 20:
        py, sy, isStand = HEIGHT - 20, 0, True

    if pressSit: dinoImage = imgDinoSit[int(frame)]
    else: dinoImage = imgDinoStand[int(frame)]

    dw, dh = dinoImage.get_width(), dinoImage.get_height()
    dinoRect = pygame.Rect(150, py - dh, dw, dh)

    for i in range(len(bgs)-1, -1, -1):
        bg = bgs[i]
        bg.x -= speed

        bg.right < 0 and bgs.pop(i)

    if bgs[-1].right < WIDTH:
        bgs.append(pygame.Rect(bgs[-1].right, HEIGHT - 50, 2400, 26))

    window.fill('white')
    for bg in bgs: window.blit(imgBG, bg)
    window.blit(dinoImage, dinoRect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
