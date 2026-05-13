# Graph Coloring Problem using CSP and Backtracking

# Graph representation
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V', 'T'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Available colors
colors = ['Red', 'Green', 'Blue']


# Function to check whether color assignment is valid
def is_valid(node, color, assignment):

    for neighbor in graph[node]:

        # Check constraint
        if neighbor in assignment and assignment[neighbor] == color:
            return False

    return True


# CSP using Backtracking
def csp(assignment):

    # If all nodes are assigned
    if len(assignment) == len(graph):
        return assignment

    # Select unassigned node
    for node in graph:
        if node not in assignment:
            break

    # Try all colors
    for color in colors:

        # Check validity
        if is_valid(node, color, assignment):

            # Assign color
            assignment[node] = color

            # Recursive call
            result = csp(assignment)

            # If solution found
            if result:
                return result

            # Backtracking step
            del assignment[node]

    return None


# Start CSP
solution = csp({})

# Display output
print("\nGraph Coloring Solution:\n")

for state, color in solution.items():
    print(state, "->", color)