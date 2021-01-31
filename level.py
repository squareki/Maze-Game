import random

from maze_generation import *
from player import *
from graphics import *

PLAYER_SPRITE = "semicolon_three.png"

class Level():
    
    def __init__(self, height, width, start):
        self.maze = Maze(height, width)
        self.player = Player(PLAYER_SPRITE, 30, 10, *start)
        self.start = start
        self.finish = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        return level

    #should this exist? should player be drawn separately from level?
    #def draw_level(level, surface):
    #    draw_maze(level.maze, surface)
        
        
