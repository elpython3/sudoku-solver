# author: @elpython3

# NOTICE:
# For those wanting to try out this script, make sure your sudoku board is formatted into a list such as the following:
# 
# empty_board = [
#     [[], [], []], [[], [], []], [[], [], []],
#     [[], [], []], [[], [], []], [[], [], []],
#     [[], [], []], [[], [], []], [[], [], []],
#     [[], [], []], [[], [], []], [[], [], []],
#     [[], [], []], [[], [], []], [[], [], []],
#     [[], [], []], [[], [], []], [[], [], []],
#     [[], [], []], [[], [], []], [[], [], []],
#     [[], [], []], [[], [], []], [[], [], []],
#     [[], [], []], [[], [], []], [[], [], []]
# ]
# 
# An example would look like this:

# demo_board = [
#     [[9], [5], [7]], [[], [1], [3]], [[2], [8], [4]],
#     [[4], [], [3]], [[], [], [7]], [[1], [9], [6]],
#     [[6], [], [2]], [[], [4], []], [[5], [], []],
#     [[], [7], []], [[], [], []], [[], [], []],
#     [[], [], []], [[9], [], [1]], [[], [], []],
#     [[], [], []], [[], [2], []], [[], [4], []],
#     [[], [], [5]], [[], [], []], [[6], [], [3]],
#     [[], [9], []], [[4], [], []], [[], [7], []],
#     [[7], [], [6]], [[], [], []], [[], [], []]
# ]

# Helper functions to get the row, column, and quadrant idx in the board format.
def row_idx(i):
    if (i+1) <= 3:
        return 0
    if (i+1) <= 6 and (i+1) > 3:
        return 1
    if (i+1) <= 9 and (i+1) > 6:
        return 2
    if (i+1) <= 12 and (i+1) > 9:
        return 3
    if (i+1) <= 15 and (i+1) > 12:
        return 4
    if (i+1) <= 18 and (i+1) > 15:
        return 5
    if (i+1) <= 21 and (i+1) > 18:
        return 6
    if (i+1) <= 24 and (i+1) > 21:
        return 7
    if (i+1) <= 27 and (i+1) > 24:
        return 8

def column_idx(i, j):
    if (i+1) % 3 == 1:
        if j == 0:
            return 0
        if j == 1:
            return 1
        if j == 2:
            return 2
    if (i+1) % 3 == 2:
        if j == 0:
            return 3
        if j == 1:
            return 4
        if j == 2:
            return 5
    if (i+1) % 3 == 0:
        if j == 0:
            return 6
        if j == 1:
            return 7
        if j == 2:
            return 8

def quadrant_idx(i):
    if (i+1) == 1 or (i+1) == 4 or (i+1) == 7:
        return 0
    if (i+1) == 2 or (i+1) == 5 or (i+1) == 8:
        return 1
    if (i+1) == 3 or (i+1) == 6 or (i+1) == 9:
        return 2
    if (i+1) == 10 or (i+1) == 13 or (i+1) == 16:
        return 3
    if (i+1) == 11 or (i+1) == 14 or (i+1) == 17:
        return 4
    if (i+1) == 12 or (i+1) == 15 or (i+1) == 18:
        return 5
    if (i+1) == 19 or (i+1) == 22 or (i+1) == 25:
        return 6
    if (i+1) == 20 or (i+1) == 23 or (i+1) == 26:
        return 7
    if (i+1) == 21 or (i+1) == 24 or (i+1) == 27:
        return 8

# Helper functions to get row, column, and quadrant.
def get_row(bo, idx):
    row = []
    for i in range(len(bo)):
        if row_idx(i) == idx:
            for j in range(len(bo[i])):
                if len(bo[i][j]) > 0:
                    row.append(bo[i][j][0])
                else:
                    row.append(0)

    return row

def get_column(bo, idx):
    column = []
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if column_idx(i, j) == idx:
                if len(bo[i][j]) > 0:
                    column.append(bo[i][j][0])
                else:
                    column.append(0)
    
    return column

def get_quadrant(bo, idx):
    quadrant = []
    for i in range(len(bo)):
        # for j in range(len(bo[i])):
        if quadrant_idx(i) == idx:
            for j in range(len(bo[i])):
                if len(bo[i][j]) > 0:
                    quadrant.append(bo[i][j][0])
                else:
                    quadrant.append(0)
    return quadrant

# Function to print the board in a cleaner format, this one is mostly used for debug.
def print_board_debug(bo):
    print(f"{bo[0]}, {bo[1]}, {bo[2]},")
    print(f"{bo[3]}, {bo[4]}, {bo[5]},")
    print(f"{bo[6]}, {bo[7]}, {bo[8]},")
    print(f"{bo[9]}, {bo[10]}, {bo[11]},")
    print(f"{bo[12]}, {bo[13]}, {bo[14]},")
    print(f"{bo[15]}, {bo[16]}, {bo[17]},")
    print(f"{bo[18]}, {bo[19]}, {bo[20]},")
    print(f"{bo[21]}, {bo[22]}, {bo[23]},")
    print(f"{bo[24]}, {bo[25]}, {bo[26]}\n")

# Function to print the board in a cleaner format, this one more fancy than the former.
def print_board(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if (j+1) % 3 == 0:
                if (i+1) % 3 != 0:
                    print(f"{bo[i][j][0]} |", end=" ")
                else:
                    print(f"{bo[i][j][0]}")
            else:
                print(f"{bo[i][j][0]} ", end="")
        if (i+1) % 9 == 0 and i < 26:
            print("---------------------")

# Solves the sudoku board.
def solve(bo):
    found_empty = find_empty(bo)
    if not found_empty:
        # This means the board is complete.
        return True
    found_i, found_j = found_empty
    
    for i in range(1, 10):
        # Check if a number from 1-9 works as a possible solution.
        if validate(bo, i, (found_i, found_j)):
            # It works so far, set the square as the value of i
            bo[found_i][found_j] = [i]

            # Implementing a bactracking algorithim.
            # Backtracking is a recursive algorithm (meaning it involves a function calling itself). In this case, the function will always call itself
            # until either the entire board is solved, or a space creates an impossible solution (eg. duplicates in a row). If the former occurs, the
            # function will thus completely stop, as all instances of the function will return True (see line 176). If the latter occurs, the function
            # instance will stop, and keep going to previous instances until another possible solution occurs (thus called a backtracking algorithm).
            if solve(bo):
                return True
            
            # It doesn't work, reset the value to empty
            bo[found_i][found_j] = []

    # Occurs if an impossible solution occurs.
    return False


# Checks if a number works in a given position on the board.
def validate(bo, num, pos):
    row = get_row(bo, row_idx(pos[0]))
    for i in range(9):
        if row[i] == num:
            return False
    
    column = get_column(bo, column_idx(pos[0], pos[1]))
    for i in range(9):
        if column[i] == num:
            return False
    
    quadrant = get_quadrant(bo, quadrant_idx(pos[0]))
    for i in range(9):
        if quadrant[i] == num:
            return False

    return True

# Look for empty spaces on the board.
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if len(bo[i][j]) == 0:
                return (i, j)
    return None


if __name__ == '__main__':
    demo_board = [
        [[9], [5], [7]], [[], [1], [3]], [[2], [8], [4]],
        [[4], [], [3]], [[], [], [7]], [[1], [9], [6]],
        [[6], [], [2]], [[], [4], []], [[5], [], []],
        [[], [7], []], [[], [], []], [[], [], []],
        [[], [], []], [[9], [], [1]], [[], [], []],
        [[], [], []], [[], [2], []], [[], [4], []],
        [[], [], [5]], [[], [], []], [[6], [], [3]],
        [[], [9], []], [[4], [], []], [[], [7], []],
        [[7], [], [6]], [[], [], []], [[], [], []]
    ]
    solve(demo_board)
    print_board(demo_board)
    # print_board_debug(demo_board)