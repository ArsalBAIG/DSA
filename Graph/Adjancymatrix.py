class Graph:

    def __init__(self, ver_count): # ver_count rep no of vertices.
        self.vertex_count = ver_count # below, * represents repeatation.
        self.adj_matrix = [[0] * ver_count for i in range(ver_count)] # It creates a list having no of zeros'0' equals to no of rows.

    def add_edge(self, u, v, weight = 1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = weight # these conditions are for undirected graphs.
            self.adj_matrix[v][u] = weight
        else:
            print('Invalid Vertix.')

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print('Invalid Vertix.')

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print('Invalid Vertix.')

    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str,row_list))) # Here, str is a function & row_list is a list inside the lists of matrix.
