from Maze_generation import *

class Player():
    
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, Direction, Maze):
        if (Maze.get_grid()[self.x_pos][self.y_pos].__contains__(Direction)):
            if (Direction == UP):
                self.x_pos += 1
            elif (Direction == DOWN):
                self.x_pos -= 1
            elif (Direction == RIGHT):
                self.y_pos += 1
            elif (Direction == LEFT):
                self.y_pos -= 1
        return self.x_pos, self.y_pos
    

m = Maze(10, 10)
board = Maze.grid
p = Player(1, 1)
print()
print("player is at [{};{}]".format(p.x_pos, p.y_pos))
print("can we move from 1,1 to right? {}".format(Maze.grid[1][1].__contains(Direction(UP))) == True)
p.move(Direction['UP'], Maze)
print("player is at [{};{}]".format(p.x_pos, p.y_pos))
p.move(Direction.LEFT, Maze)
print("player is at [{};{}]".format(p.x_pos, p.y_pos))
p.move(Direction.DOWN, Maze)
print("player is at [{};{}]".format(p.x_pos, p.y_pos))
