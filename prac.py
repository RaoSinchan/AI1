

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        # Heuristic values can be updated based on user input if needed
        H = {node: 1 for node in self.adjacency_list}  # default 1 for all
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):  
        open_list = set([start_node])
        closed_list = set([])
        g = {start_node: 0}
        parents = {start_node: start_node}

        while open_list:
            n = None
            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v   

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start_node)
                path.reverse()
                print('Path found: {}'.format(path))
                return path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


# -------- User Input Section --------
adjacency_list = {}

num_nodes = int(input("Enter number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = []
    num_neighbors = int(input(f"Enter number of neighbors for {node}: "))
    for _ in range(num_neighbors):
        neighbor = input(f"Enter neighbor of {node}: ")
        weight = int(input(f"Enter weight from {node} to {neighbor}: "))
        neighbors.append((neighbor, weight))
    adjacency_list[node] = neighbors

start_node = input("Enter start node: ")
stop_node = input("Enter stop node: ")

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm(start_node, stop_node)
