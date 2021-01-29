import pygame
# from maze_generation import *

def draw_maze(maze, surface):
    cell_size = 30
    color = (0, 244, 244)
    border_color = (10, 10, 10)
    padding = 10
    
    pygame.draw.rect(surface, border_color, (0, 0, padding, padding))
    pygame.draw.rect(surface, border_color, (padding, 0, maze.width * (cell_size + padding), padding))
    pygame.draw.rect(surface, border_color, (0, padding, padding,maze.height * (cell_size + padding)))

    for i in range(maze.height):
        for j in range(maze.width):
            cell = maze.grid[i][j]
            cell_x, cell_y = padding + (padding + cell_size) * j, padding + (padding + cell_size) * i
            pygame.draw.rect(surface, color, (cell_x, cell_y, cell_size, cell_size))
            
            if Direction.RIGHT in cell:
                border_color = color
            pygame.draw.rect(surface, border_color, (cell_x + cell_size, cell_y, padding, cell_size))
            border_color = (0, 0, 0)
            
            if Direction.DOWN in cell:
                border_color = color
            pygame.draw.rect(surface, border_color, (cell_x, cell_y + cell_size, cell_size, padding))
            border_color = (0, 0, 0)
            
            pygame.draw.rect(surface, border_color, (cell_x + cell_size, cell_y + cell_size, padding, padding))

            
    pygame.display.update()
    
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

BLUE = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(BLUE)
running = True

m = Maze(8, 12)

draw_maze(m, screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False
    pygame.display.flip()

pygame.display.quit()
pygame.quit()
