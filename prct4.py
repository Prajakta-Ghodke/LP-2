# Map Coloring Problem

# List of states
states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Adjacency list
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Dictionary to store result
result = {}

# Function to check whether color assignment is safe
def is_safe(state, color):

    for neighbour in neighbors[state]:

        if neighbour in result and result[neighbour] == color:
            return False

    return True

# Assign colors to states
for state in states:

    for color in colors:

        if is_safe(state, color):
            result[state] = color
            break

# Display solution
print("Map Coloring Solution:")

for state in result:
    print(state, '->', result[state])