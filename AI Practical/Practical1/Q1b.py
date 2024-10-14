from collections import deque

# Graph definition
graph1 = {
    'a': set(['b', 'c']),
    'b': set(['a', 'd', 'e']),
    'c': set(['a', 'f']),
    'd': set(['b']),
    'e': set(['b', 'f']),
    'f': set(['c', 'e'])
}

def bfs(graph, start):
    visited = []  # List to keep track of visited nodes
    queue = deque([start])  # Use deque as a queue for BFS

    while queue:
        node = queue.popleft()  # Remove and return the leftmost element
        if node not in visited:
            visited.append(node)  # Mark node as visited
            queue.extend(graph[node] - set(visited))  # Add unvisited neighbors to the queue
    
    return visited

# Start BFS from node 'a'
v = bfs(graph1, 'a')
print(v)
