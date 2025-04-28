# Taking input for the graph
graph = {}
n = int(input("Enter the number of nodes: "))

for _ in range(n):
    node = input("Enter the node: ")
    neighbours = input(f"Enter the neighbours of {node} separated by space: ").split()
    graph[node] = neighbours

print(graph)
# BFS implementation
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph.get(s, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# DFS implementation
visited_dfs = set()
    
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

# Driver code
start_node = input("Enter the starting node for traversal: ")

print("\nBreadth-First Search:")
bfs(visited, graph, start_node)

print("\n\nDepth-First Search:")
dfs(visited_dfs, graph, start_node)
