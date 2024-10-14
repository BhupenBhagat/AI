from collections import deque
graph1={
    'a':set(['b','c']),
    'b':set(['a','d','e']),
    'c':set(['a','f']),
    'd':set(['b']),
    'e':set(['b','f']),
    'f':set(['c','e'])
}
def bfs(graph,start):
    visited=[]
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph1[node]-set(visited))
    return visited

v=bfs(graph1,'a')
print(v)