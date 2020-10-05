maze = [
    [3, 1, 5],
    [2, 1, 1],
    [7, 8, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, -1],
]

moves_taken = []

def a_star(y, x):
    combos = [
        (y, x - 1),
        (y, x + 1),
        (y - 1, x),
        (y - 1, x - 1),
        (y - 1, x + 1),
        (y + 1, x - 1),
        (y + 1, x),
        (y + 1, x + 1),
    ]
    possible_moves = []
    lowest_node = None

    for y_pos, x_pos in combos:
        try:
            if x_pos == -1 and y_pos == -1:
                continue
            else:
                possible_moves.append((y_pos, x_pos, maze[y_pos][x_pos]))
        except:
            # Out of bounds error, not a valid node to traverse
            pass
    
    # We find the lowest cost
    for move in possible_moves:
        if lowest_node == None or lowest_node[2] >= move[2]: # Should be > not >=
            lowest_node = move

    element = (lowest_node[0], lowest_node[1])

    # Check if we are at target node -> if we are, stop otherwise recursively call the function
    if lowest_node[2] == -1:
        moves_taken.append(element)
    elif lowest_node != None:
        moves_taken.append(element)
        lowest_node = None
        a_star(element[0], element[1])

    return moves_taken

print(a_star(2, 2))