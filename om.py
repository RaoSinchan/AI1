class Graph:
    def __init__(self,adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbour(self,v):
        return self.adjacency_list[v]
    
    def h(self,n):
        H={
            'A':1,
            'B':1,
            'C':1,
            'D':1
        }
        return H[n]
    
    def a_star(self,start_node,stop_node):
        open_list=set([start_node])
        close_list=set([])
        g={start_node:0}
        parents={start_node:start_node}
        
        while open_list:
            n =None
            for v in open_list:
                if n is None or g[v]+self.h(v)<g[n]+self.h(n):
                    n=v

            
            if n is None:
                print('Path does not exist!')
                return None
            
            if n==stop_node:
                path=[]
                while parents[n]!=n:
                    path.append(n)
                    n=parents[n]
                path.append(start_node)
                path.reverse()
                print("path found {}".format(path))
                return path

            for (m,weight) in self.get_neighbour(n):
                if m not in open_list and m not in close_list:
                    open_list.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if(g[m]>g[n]+weight):
                        g[m]=g[n]+weight
                        parents[m]=n
                        if m in close_list:
                            close_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            close_list.add(n)

        print('Path does not exist!')
        return None

adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

graph1=Graph(adjacency_list)
graph1.a_star('A','D')
