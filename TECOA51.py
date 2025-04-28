class GraphColoring:
    def __init__(self, graph, max_colors):
        self.graph = graph  
        self.num_vertices = len(graph)
        self.max_colors = max_colors
        self.colors = [-1] * self.num_vertices 

    def is_safe(self, vertex, color):
        for neighbor in range(self.num_vertices):
            if self.graph[vertex][neighbor] == 1 and self.colors[neighbor] == color:
                return False
        return True

    def branch_and_bound(self, vertex=0):
        if vertex == self.num_vertices:
            return True
        
        for color in range(1, self.max_colors + 1):
            if self.is_safe(vertex, color):
                self.colors[vertex] = color
                if self.branch_and_bound(vertex + 1):  
                    return True
                self.colors[vertex] = -1  
        
        return False
    
    def solve(self):
        if not self.branch_and_bound():
            print("Solution does not exist")
        else:
            print("Solution found: ", self.colors)


graph = [
    [0, 1, 1, 0], 
    [1, 0, 1, 0],  
    [1, 1, 0, 1],  
    [0, 0, 1, 0],]

max_colors = 3  

graph_coloring = GraphColoring(graph, max_colors)
graph_coloring.solve()


