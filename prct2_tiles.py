# Simple A* Algorithm for 8 Puzzle

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]


# Heuristic Function
# Count misplaced tiles
def heuristic(state):

    count = 0

    for i in range(9):

        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


# Print puzzle
def print_state(state):

    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])

    print()


# Open list stores (state, g(n))
open_list = [(start, 0)]

visited = []

print("----- A* Algorithm for 8 Puzzle -----\n")

while open_list:

    # Sort using f(n)=g(n)+h(n)
    open_list.sort(key=lambda x: x[1] + heuristic(x[0]))

    current, g = open_list.pop(0)

    print("Current State:")
    print_state(current)

    h = heuristic(current)
    f = g + h

    print("g(n) =", g)
    print("h(n) =", h)
    print("f(n) =", f)
    print()

    # Goal Check
    if current == goal:

        print("Goal State Reached")
        break

    visited.append(current)

    # Find blank position
    blank = current.index(0)

    # Possible moves
    moves = []

    if blank - 3 >= 0:
        moves.append(blank - 3)

    if blank + 3 < 9:
        moves.append(blank + 3)

    if blank % 3 != 0:
        moves.append(blank - 1)

    if blank % 3 != 2:
        moves.append(blank + 1)

    # Generate next states
    for move in moves:

        new_state = current.copy()

        new_state[blank], new_state[move] = new_state[move], new_state[blank]

        if new_state not in visited:

            open_list.append((new_state, g + 1))