from maze_generation import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image, size, padding, x_pos, y_pos):
        super(Player, self).__init__()
        self.surf = pygame.image.load(image).convert()
        self.surf = pygame.transform.scale(self.surf, (size, size))
        self.rect = self.surf.get_rect()
        self.rect = self.rect.move(x_pos, y_pos)
        self.step_len = size + padding
        self.x_pos, self.y_pos = 0, 0
        

    def move(self, direction, cell):
        if direction in cell:
            if (direction == Direction.UP):
                self.rect = self.rect.move(0, -self.step_len)
                self.y_pos -= 1
            elif (direction == Direction.DOWN):
                self.rect = self.rect.move(0, self.step_len)
                self.y_pos += 1
            elif (direction == Direction.RIGHT):
                self.rect = self.rect.move(self.step_len, 0)
                self.x_pos += 1
            else:  # direction == Direction.LEFT
                self.rect = self.rect.move(-self.step_len, 0)
                self.x_pos -= 1
    


# m = Maze(10, 10)
# m.print_maze()
# board = m.grid
# p = Player(1, 1)
# print()
# print("player is at [{};{}]".format(p.x_pos, p.y_pos))
# print("can we move from 1,1 to right? {}".format(Direction.RIGHT in m.grid[1][1]))
# p.move(Direction.UP, m)
# print("player is at [{};{}]".format(p.x_pos, p.y_pos))
# p.move(Direction.LEFT, m)
# print("player is at [{};{}]".format(p.x_pos, p.y_pos))
# p.move(Direction.DOWN, m)
# print("player is at [{};{}]".format(p.x_pos, p.y_pos))
