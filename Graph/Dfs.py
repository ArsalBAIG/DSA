def  dfs(graph, start, visited= None):
    if visited is None:
        visited = set() # Here, we initilized an empty set to store the visited nodes.
    visited.add(start)
    print(start)

    for neighbor in graph[start]: # this iterates the neighbors of start node.
        if neighbor not in visited:
            dfs(graph, neighbor, visited)# It recursively calls the dfs func as that missing neighbor as a start node.

    return visited

graph = {
    '0' : set(['1', '2']), # Here, key rep the nodes and values are sets of adj nodes.
    '1' : set(['0','3', '4']),
    '2' : set(['0']),
    '3' : set(['1']),
    '4' : set(['2', '3'])
}

dfs(graph, '0')