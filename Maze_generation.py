import random
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Maze():
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
    
    class Bitset():
        def __init__(self):
            self.directions = 0
            # 1 is up, 2 is down, 3 is left, 4 is right
        
        def __contains__(self, direction):
            return self.directions & (1 << direction)
        
        def add_direction(self, direction):
            self.directions |= (1 << direction)
    
    def build_maze(self):
        edge_graph = []
        row_size = len(self.grid[0])
        
        for i in range(len(self.grid)):
            for j in range(row_size - 1):
                edge_graph.append((j + i * row_size, j + 1 + i * row_size))
        for i in range(len(self.grid) - 1):
            for j in range(row_size):
                edge_graph.append((j + i * row_size, j + (i + 1) * row_size))
                
        random.shuffle(edge_graph)
        
        
        for u, v in edge_graph:
            if self.disjoint_set.find(u) != self.disjoint_set.find(v):
                self.disjoint_set.union(u, v)
                if v - u == 1:
                    self.grid[u // row_size][u % row_size].add_direction(self.direction["right"])
                else:
                    self.grid[u // row_size][u % row_size].add_direction(self.direction["down"])
                    
        
        [print(' _', end = '') for i in range(row_size)]
        for row in self.grid:
            print('\n', '│', sep = '', end = '')
            for elem in row:
                if not self.direction['down'] in elem:
                    print('_', end = '')
                else:
                    print(' ', end = '')
                if not self.direction['right'] in elem:
                    print('│', end = '')
                else:
                    print(' ', end = '')

                
    
    def __init__(self, maze_height, maze_width):
        self.maze_height = maze_height
        self.maze_width = maze_width
        self.grid = [[self.Bitset() for j in range(maze_width)] for i in range(maze_height)]
        self.disjoint_set = self.disjoint_set_union(maze_height * maze_width)
        self.direction = {"down" : 2, "right" : 4}
        self.build_maze()
        

    def get_grid(self):
        return self.grid
    

#m = Maze(20, 20)
