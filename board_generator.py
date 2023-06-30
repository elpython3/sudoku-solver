from random import sample, randrange

import backtrack_sudoku_solver

base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c):
    return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)

def shuffle(s):
    return sample(s,len(s))

def gen_board():
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    squares = side*side
    empties = squares * randrange(40, 65)//81
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0

    return board

# for line in gen_board():
    # print(line)
def format(board):
    bo = []
    for i in range(len(board)):
        for j in range(3):
            subset = []
            for k in range(3):
                # if j == 0:
                if board[i][(3*j)+k] != 0:
                    subset.append([board[i][(3*j)+k]])
                    # print(board[i][(3*j)+k])
                else:
                    # print("e")
                    subset.append([])
            bo.append(subset)
    return bo

# board = gen_board()
# formatted_board = format(board)

# print(formatted_board)
# backtrack_sudoku_solver.print_board_debug(formatted_board)
# backtrack_sudoku_solver.solve(formatted_board)
# backtrack_sudoku_solver.print_board(formatted_board)

#
# numSize = len(str(side))
# for line in board:
#     print(*(f"{n or '.':{numSize}} " for n in line))

# test_list = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]

# test_list_1 = []
# for i in range(len(test_list)):
#     for j in range(3):
#         subset = []
#         for k in range(3):
#             # if j == 0:
#             subset.append(test_list[i][(3*j)+k])
#         test_list_1.append(subset)
# print(test_list_1)