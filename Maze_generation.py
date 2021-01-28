import random
from enum import Enum

class Direction(Enum):
    __order__ = "UP DOWN LEFT RIGHT"
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    

class disjoint_set_union():
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [i for i in range(size)]
        
    def find(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.size[v] < self.size[u]:
                u, v = v, u
            self.parent[u] = v
            self.size[v] += self.size[u]
                
                
class Maze():
    class Bitset():
        def __init__(self):
            self.directions = 0
        
        def __contains__(self, direction):
            return self.directions & (1 << direction)
        
        def __str__(self):
            res = []
            if not Direction.DOWN.value in self:
                res.append('_')
            else:
                res.append(' ')
            if not Direction.RIGHT.value in self:
                res.append('│')
            else:
                res.append(' ')
            return ''.join(res)
        
        def add_direction(self, direction):
            self.directions |= (1 << direction)
    
    def print_maze(self):
        [print(' _', end = '') for i in range(self.maze_width)]
        for row in self.grid:
            print('\n', '│', sep = '', end = '')
            for elem in row:
                print(elem, end = '')
    
    def build_maze(self):
        edge_graph = []
        
        for i in range(self.maze_height):
            for j in range(self.maze_width - 1):
                edge_graph.append((j + i * self.maze_width, j + 1 + i * self.maze_width))
        for i in range(self.maze_height - 1):
            for j in range(self.maze_width):
                edge_graph.append((j + i * self.maze_width, j + (i + 1) * self.maze_width))
        
        random.shuffle(edge_graph)
        
        for u, v in edge_graph:
            if self.disjoint_set.find(u) != self.disjoint_set.find(v):
                self.disjoint_set.union(u, v)
                if v - u == 1:
                    self.grid[u // self.maze_width][u % self.maze_width].add_direction(Direction.RIGHT.value)
                else:
                    self.grid[u // self.maze_width][u % self.maze_width].add_direction(Direction.DOWN.value)                
    
    def __init__(self, maze_height, maze_width):
        self.maze_height = maze_height
        self.maze_width = maze_width
        self.grid = [[self.Bitset() for j in range(maze_width)] for i in range(maze_height)]
        self.disjoint_set = disjoint_set_union(maze_height * maze_width)
        self.build_maze()
    

m = Maze(20, 20)
# m.print_maze()
