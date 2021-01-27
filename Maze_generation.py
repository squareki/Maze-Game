class Maze():
    class disjoint_set_union():
        def __init__(self, size):
            self.parent = [i for i in range(size)]
            self.set_size = [i for i in range(size)]
            
        def find(self, v):
            if self.parent[v] == v:
                return v
            self.parent[v] = find(self.parent[v])
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
            return (self.directions & (1 << direction)) != 0
        
        def add_direction(self, direction: str):
            self.directions |= (1 << direction)
    
    def build_maze(self):
        edge_graph = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0]) - 1):
                edge_graph.append((j + i * len(self.grid[0]), j + 1 + i * len(self.grid[0])))
        for i in range(len(self.grid) - 1):
            for j in range(len(self.grid[0])):
                edge_graph.append((j + i * len(self.grid[0]), j + (i + 1) * len(self.grid[0])))
                
        random.shuffle(edge_graph)
        
        print(edge_graph)
        
        for u, v in edge_graph:
            if self.disjoint_set.find(u) != self.disjoint_set.find(v):
                self.disjoint_set.union(u, v)
        
                
    
    def __init__(self, maze_height, maze_width):
        self.maze_height = maze_height
        self.maze_width = maze_width
        self.grid = [[self.Bitset() for j in range(maze_width)] for i in range(maze_height)]
        self.disjoint_set = self.disjoint_set_union(maze_height * maze_width)
        self.direction = {"up" : 1, "down" : 2, "left" : 3, "right" : 4}
        self.build_maze()
        


# m = Maze(10, 10)
