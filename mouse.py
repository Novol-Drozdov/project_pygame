import pygame
pygame.init()

WiDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WiDTH, HEIGHT))
clock = pygame.time.Clock()

def drawCursor(x, y):
    pygame.draw.circle(window, (255, 255, 255), (x, y), 20, 1)
    pygame.draw.circle(window, (255, 255, 255), (x, y), 1)
    pygame.draw.line(window, (255, 255, 255), (x - 24, y), (x - 16, y))
    pygame.draw.line(window, (255, 255, 255), (x + 24, y), (x + 16, y))
    pygame.draw.line(window, (255, 255, 255), (x, y - 24), (x, y - 16))
    pygame.draw.line(window, (255, 255, 255), (x, y + 24), (x, y + 16))

cursorPX, cursorPY = WiDTH // 2, HEIGHT // 2 - 200

pygame.mouse.set_visible(False)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    cursorPX, cursorPY = pygame.mouse.get_pos()
    buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()
    print(buttonLeft, buttonMiddle, buttonRight)
    window.fill(pygame.Color('black'))
    drawCursor(cursorPX, cursorPY)
    drawCursor(300, 400)
   

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
