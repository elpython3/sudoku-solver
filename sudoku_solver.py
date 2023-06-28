# Author: elpython3

# This is an older verson of a sudoku solver, and did not use backtracking. This script generally works, but if given too little information
# it will lead into a RecursionError, thus being less efficient than the newer version.

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
# 
# Be aware that it will need enough information (you need more than 17 numbers and all the numbers have to be placed in a specific manner) or
# the script will end up in a RecursionError.


board = [
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []]
]

board1 = [
    [[], [3], []], [[], [], []], [[], [8], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [7], []], [[], [], []],
    [[], [], []], [[5], [], []], [[], [], [2]],
    [[8], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], [9]], [[6], [], []],
    [[], [4], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [1], []], [[], [], []]
]

full_board = [
    [[9], [5], [7]], [[6], [1], [3]], [[2], [8], [4]],
    [[4], [8], [3]], [[2], [5], [7]], [[1], [9], [6]],
    [[6], [1], [2]], [[8], [4], [9]], [[5], [3], [7]],
    [[1], [7], [8]], [[3], [6], [4]], [[9], [5], [2]],
    [[5], [2], [4]], [[9], [7], [1]], [[3], [6], [8]],
    [[3], [6], [9]], [[5], [2], [8]], [[7], [4], [1]],
    [[8], [4], [5]], [[7], [9], [2]], [[6], [1], [3]],
    [[2], [9], [1]], [[4], [3], [6]], [[8], [7], [5]],
    [[7], [3], [6]], [[1], [8], [5]], [[4], [2], [9]]
]


easy_board = [
    [[9], [5], [7]], [[], [1], [3]], [[2], [8], [4]],
    [[4], [8], [3]], [[2], [5], [7]], [[1], [9], [6]],
    [[6], [], [2]], [[8], [4], [9]], [[5], [3], [7]],
    [[1], [7], [8]], [[3], [6], [4]], [[9], [5], [2]],
    [[5], [2], [4]], [[9], [7], [1]], [[3], [6], [8]],
    [[3], [6], [9]], [[5], [2], [8]], [[7], [4], [1]],
    [[8], [4], []], [[7], [9], [2]], [[6], [1], [3]],
    [[2], [9], [1]], [[4], [3], [6]], [[8], [7], [5]],
    [[7], [3], [6]], [[1], [8], [5]], [[4], [2], [9]]
]

easy_board_1 = [
    [[], [], [7]], [[], [1], [3]], [[2], [8], [4]],
    [[4], [], [3]], [[2], [5], [7]], [[1], [], [6]],
    [[6], [], []], [[], [4], [9]], [[5], [], [7]],
    [[], [7], []], [[], [6], [4]], [[], [], [2]],
    [[], [], []], [[9], [], [1]], [[3], [6], [8]],
    [[], [], []], [[5], [2], [8]], [[], [], [1]],
    [[], [], []], [[], [], [2]], [[], [], [3]],
    [[], [9], [1]], [[], [], []], [[8], [7], [5]],
    [[7], [3], []], [[], [], []], [[], [2], [9]]
]

demo_board = [
    [[], [], []], [[], [], []], [[2], [], []],
    [[], [8], []], [[], [], [7]], [[], [9], []],
    [[6], [], [2]], [[], [], []], [[5], [], []],
    [[], [7], []], [[], [6], []], [[], [], []],
    [[], [], []], [[9], [], [1]], [[], [], []],
    [[], [], []], [[], [2], []], [[], [4], []],
    [[], [], [5]], [[], [], []], [[6], [], [3]],
    [[], [9], []], [[4], [], []], [[], [7], []],
    [[], [], [6]], [[], [], []], [[], [], []]
]

# demo_board = [
#     [[9], [5], [7]], [[], [1], [3]], [[2], [8], [4]],
#     [[4], [], [3]], [[], [], [7]], [[1], [9], [6]],
#     [[6], [], [2]], [[], [], []], [[5], [], []],
#     [[], [7], []], [[], [6], []], [[], [], []],
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
    
# Function to print the board in a cleaner format
def print_board(board):
    print(f"{board[0]}, {board[1]}, {board[2]},")
    print(f"{board[3]}, {board[4]}, {board[5]},")
    print(f"{board[6]}, {board[7]}, {board[8]},")
    print(f"{board[9]}, {board[10]}, {board[11]},")
    print(f"{board[12]}, {board[13]}, {board[14]},")
    print(f"{board[15]}, {board[16]}, {board[17]},")
    print(f"{board[18]}, {board[19]}, {board[20]},")
    print(f"{board[21]}, {board[22]}, {board[23]},")
    print(f"{board[24]}, {board[25]}, {board[26]}\n")


# Solves the sudoku board.
# This version of the solver uses recursion, but does not implement backtracking. It works by taking solved squares and removing the value of each 
# square from each unsolved square which would cause an impossible solution otherwise, doing so all at once instead of one square at a time.
# This proves to be ineffective as in some cases all of the solved squares are removed from the possiblilties of the other unsolved squares,
# but may not create more solved squares.
def solve(board = [
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []],
    [[], [], []], [[], [], []], [[], [], []]
]):
    row_certains = [
        [], [], [], [], [], [], [], [], []
    ]
    column_certains = [
        [], [], [], [], [], [], [], [], []
    ]
    quadrant_certains = [
        [], [], [], [], [], [], [], [], []
    ]

    # Looks for solved squares.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(board[i][j]) == 1:
                row_certains[row_idx(i)].append(board[i][j][0])
                column_certains[column_idx(i, j)].append(board[i][j][0])
                quadrant_certains[quadrant_idx(i)].append(board[i][j][0])
    
    # Remove the value of solved squares from the possibilities of unsolved squares based on sudoku rules.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(board[i][j]) != 1:
                append_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for k in row_certains[row_idx(i)]:
                    if k in append_list:
                        append_list.remove(k)
                for l in column_certains[column_idx(i, j)]:
                    if l in append_list:
                        append_list.remove(l)
                for m in quadrant_certains[quadrant_idx(i)]:
                    if m in append_list:
                        append_list.remove(m)
                board[i][j] = append_list

    # Check if the board is filled. If not, call solve() again.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(board[i][j]) != 1:
                try:
                    solve(board=board)
                    break
                except RecursionError:
                    print("Recursion Error occured. Most likely unable to recover.")
                    exit()
    else:
        return

solve(demo_board)
print_board(demo_board)

