graph1={
    'a':set(['b','c']),
    'b':set(['a','d','e']),
    'c':set(['a','f']),
    'd':set(['b']),
    'e':set(['b','f']),
    'f':set(['c','e'])
}
def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n,visited)
    return visited

v=dfs(graph1,'a',[])
print(v)