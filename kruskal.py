# Disjoint Set (Union-Find) Class
class DisjointSet:
    def __init__(self, vertices):  # <-- corrected
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


# Kruskal's Algorithm
def kruskal(graph_edges, vertices):
    graph_edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(vertices)
    mst = []

    for u, v, weight in graph_edges:
        if ds.find(u) != ds.find(v):    
            ds.union(u, v)
            mst.append((u, v, weight))

    return mst

# --- Main program ---
vertices = []
edges = []

n = int(input("Enter the number of vertices: "))
for i in range(n):
    v = input(f"Enter name of vertex {i+1}: ").upper()
    vertices.append(v)

e = int(input("Enter the number of edges: "))
for i in range(e):
    u = input(f"Enter the starting vertex of edge {i+1}: ").upper()
    v = input(f"Enter the ending vertex of edge {i+1}: ").upper()
    w = int(input(f"Enter the weight of edge {u}-{v}: "))
    edges.append((u, v, w))

# Find MST
mst_result = kruskal(edges, vertices)

# Print the MST
print("\nEdges in the Minimum Spanning Tree (MST):")
for u, v, weight in mst_result:
    print(f"{u} - {v}: {weight}")