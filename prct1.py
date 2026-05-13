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

queue = []
visited_bsf = []
# BFS without using import
def bfs():
    if not queue:
        return
    
    node = queue.pop(0)
    print(node, end=' ')
    
    for neighbour in graph[node]:
        if neighbour not in visited_bsf:
            visited_bsf.append(neighbour)
            queue.append(neighbour)
    
    bfs()

start = 'A'

# Main Program
print("DFS Traversal:")
dfs('A')

visited_bsf.append(start)
queue.append(start)

print("\nBFS Traversal:")
bfs()