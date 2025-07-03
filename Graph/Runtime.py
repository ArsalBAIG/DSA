def DFS(graph, start, visited= None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for neighbors in graph[start]:
        if neighbors not in visited:
            DFS(graph, neighbors, visited)
    
    return visited

graph = {
    '1' : set(['2', '3']),
    '2' : set(['1', '3']),
    '3' : set(['1', '2', '1']),
    '4' : set(['3', '7', '1', '0'])
}

DFS(graph, '1')