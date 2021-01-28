from maze_generation import *

class Player():
    
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, direction, maze):
        if direction in maze.grid[self.x_pos][self.y_pos]:
            if (direction == Direction.UP):
                self.x_pos -= 1
            elif (direction == Direction.DOWN):
                self.x_pos += 1
            elif (direction == Direction.RIGHT):
                self.y_pos += 1
            elif (direction == Direction.LEFT):
                self.y_pos -= 1
        return self.x_pos, self.y_pos
    


m = Maze(10, 10)
m.print_maze()
board = m.grid
p = Player(1, 1)
print()
print("player is at [{};{}]".format(p.x_pos, p.y_pos))
print("can we move from 1,1 to right? {}".format(Direction.RIGHT in m.grid[1][1]))
p.move(Direction.UP, m)
print("player is at [{};{}]".format(p.x_pos, p.y_pos))
p.move(Direction.LEFT, m)
print("player is at [{};{}]".format(p.x_pos, p.y_pos))
p.move(Direction.DOWN, m)
print("player is at [{};{}]".format(p.x_pos, p.y_pos))
