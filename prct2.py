# Easy A* Algorithm

# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Goal node
goal = 'F'

# Open list and visited list
open_list = ['A']
visited = []

# A* Traversal
while open_list:

    # Remove first node from open list
    current = open_list.pop(0)

    print("Current Node =", current)

    # Goal check
    if current == goal:
        print("Goal Reached")
        break

    # Visit neighbours
    for neighbour in graph[current]:

        if neighbour not in visited and neighbour not in open_list:

            # Heuristic calculation h(n)
            h = abs(ord(goal) - ord(neighbour))

            print("Neighbour =", neighbour)
            print("Heuristic h(n) =", h)

            open_list.append(neighbour)

    # Mark current node as visited
    visited.append(current)