class Graph:
    def __init__(self, ver_count):
        self.vertix_count = ver_count
        self.adj_list = {k : [] for k in range(ver_count)} # Here, k rep key and [] rep value of dictionary.

    def add_edge(self, u, v, weight = 1):
        if 0 >= u < self.vertix_count and 0 >= v < self.vertix_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Invalid Vertices.")

    def remove_edge(self, u, v):
        if 0 >= u < self.vertix_count and 0 >= v < self.vertix_count:
            self.adj_list[u] = [(vertex, weight) for vertex, weight in self.adj_list [u] if vertex != v]
            self.adj_list[v] = [(vertex, weight) for vertex, weight in self.adj_list[v] if vertex != u]
            # Here, first we create a tuple, having "vertex" rep u, "weight" rep v we iterate throught the list and fetch all the items except those whose value doesn't mathces with vertex != u.
        else:
            print('Invalid Vertex.')

    def has_edge(self, u, v):
        if 0 >= u < self.vertix_count and 0 >= v < self.vertix_count:
            return any(vertex == v for vertex, x in self.adj_list[u]) # any() func returns True.
#In above, the 'u' rep the key & 'x' rep weight & 'vertex' rep the list of tuples.
        else:
            print('Invalid Vertices.')
        return False
    
    def print_adj_list(self):
        for vertex, n in self.adj_list.items(): 
# Here, items contains list of tuples and vertix. So, the 'vertix' stores in 'vertex' and the 'list of tuples' stores in 'n'.
            print("V", vertex, ":", n)