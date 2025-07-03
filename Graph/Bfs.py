import collections # collections has build-in datatypes tuple, set, list etc.
def bfs(graph, root): # visited is a set to keep the track of nodes.
                    # collections.deque([]) is a operation use to insert at both ends
    visited, queue = set(), collections.deque([root]) # set() has unique collection of elements.
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end=" ") # this prints the node on the output.
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour) #This, lines adds the neighbours to the visited set.
                queue.append(neighbour)# This lines adds the neighbours to the queue.

graph = {
    0: [1, 2], # This represents the node 0 is connected with node 1, 2.
    1: [2],
    2: [3],
    3: [1,2]
    }
print("BFS Traversial is: ")
bfs(graph, 0) # 0 indicates the starting node.