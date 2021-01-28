import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

BLUE = (0, 0, 200)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(BLUE)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False
    pygame.display.flip()

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(40,40,80,80))

    pygame.display.update()

pygame.display.quit()
pygame.quit()
