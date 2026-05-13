# Simple A* Algorithm using Manhattan Distance

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]


# Manhattan Distance Heuristic
def heuristic(state):

    h = 0

    for i in range(9):

        if state[i] != 0:

            goal_pos = goal.index(state[i])

            h += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)

    return h


# Print Puzzle
def print_state(state):

    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])

    print()


open_list = [(start, 0)]

visited = []

print("----- A* Algorithm -----\n")

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

    # Goal check
    if current == goal:

        print("Goal State Reached")
        break

    visited.append(current)

    blank = current.index(0)

    # Generate moves
    for move in [blank-3, blank+3, blank-1, blank+1]:

        if 0 <= move < 9:

            new_state = current.copy()

            new_state[blank], new_state[move] = new_state[move], new_state[blank]

            if new_state not in visited:

                open_list.append((new_state, g + 1))