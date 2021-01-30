import pygame
from maze_generation import *
from player import *

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
LIGHT_BLUE = (0, 244, 244)
PINK = (252, 180, 213)
BROWN = (220, 88, 5)
YELLOW = (255, 255, 0)
GOLD = (249, 166, 2)
DUSTY = (207, 181, 59)

def draw_maze(maze, surface):
    cell_size = 30
    color = PINK
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
            border_color = (10, 10, 10)

            if Direction.DOWN in cell:
                border_color = color
            pygame.draw.rect(surface, border_color, (cell_x, cell_y + cell_size, cell_size, padding))
            border_color = (10, 10, 10)

            pygame.draw.rect(surface, border_color, (cell_x + cell_size, cell_y + cell_size, padding, padding))

    
WINDOW_HEIGHT = 330
WINDOW_WIDTH = 490

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(GREY)
running = True

m = Maze(8, 12)

background = screen.copy()
draw_maze(m, background)

player = Player("semicolon_three.png", 30, 10, 10, 10)
p_start_x, p_start_y = 0, 0

screen.blit(background, (0, 0))
screen.blit(player.surf, player.rect)
pygame.display.flip()

while running:
    cur_cell = m.grid[player.y_pos + p_start_y][player.x_pos + p_start_x]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.move(Direction.UP, cur_cell)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.move(Direction.DOWN, cur_cell)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.move(Direction.LEFT, cur_cell)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.move(Direction.RIGHT, cur_cell)

    screen.fill(GREY)
    screen.blit(background, (0, 0))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

pygame.display.quit()
pygame.quit()
