# Graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS using recursion
visited = []

def dfs(node):
    if node not in visited:
        print(node, end=' ')
        visited.append(node)

        for neighbour in graph[node]:
            dfs(neighbour)

# BFS without using import
def bfs(start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Main Program
print("DFS Traversal:")
dfs('A')

print("\nBFS Traversal:")
bfs('A')