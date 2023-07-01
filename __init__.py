from flask import Flask, render_template, request, redirect, flash, session

import backtrack_sudoku_solver as bt_ss
import board_generator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hahathisissosecretlol12345'


def solve_board_from_table():
    board = []
    for i in range(9):
        subset = []
        for j in range(9):
            cell_name = f'cell-{i}-{j}'
            try:
                cell_value = int(request.form.get(cell_name, '0'))
                subset.append(cell_value)
            except ValueError:
                subset.append(0)
        board.append(subset)

    formatted_board = board_generator.format(board)

    
    # Call the Sudoku solver function to solve the board
    bt_ss.solve(formatted_board)
    solved_board = bt_ss.format_back(formatted_board)
    return solved_board

def is_valid(i, j):
    board = []
    for i in range(9):
        subset = []
        for j in range(9):
            cell_name = f'cell-{i}-{j}'
            try:
                cell_value = int(request.form.get(cell_name, '0'))
                subset.append(cell_value)
            except ValueError:
                subset.append(None)
        board.append(subset)

    if board[i][j] == session['full_board'][i][j]:
        return True
    else:
        return False

@app.route("/", methods=['POST', 'GET'])  # this sets the route to this page
def home():
    board = board_generator.gen_board()

    if 'full_board' not in session:
        session['full_board'] = board
    
    if 'incorrect_list' not in session:
        session['incorrect_list'] = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                board[i][j] = None
    
    return render_template("home.html", board=board, incorrect_list=[])
    # return redirect("/solver")

@app.route("/solver", methods=['POST', 'GET'])  # this sets the route to this page
def solver():
    board = board_generator.gen_board()

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                board[i][j] = None

    return render_template("solver.html", board=board)

@app.route("/gen-play", methods=['POST', 'GET'])
def gen_play():
    return redirect("/")

@app.route("/gen", methods=['POST', 'GET'])
def generate():
    return redirect("/solver")

@app.route('/solve', methods=['POST', 'GET'])
def solve():
    # Retrieve the Sudoku board data from the form
    solved_board = solve_board_from_table()
    return render_template('solver.html', board=solved_board)

@app.route('/check', methods=['POST', 'GET'])
def check():
    full_board = session['full_board']
    
    board = []
    for i in range(9):
        subset = []
        for j in range(9):
            cell_name = f'cell-{i}-{j}'
            try:
                cell_value = int(request.form.get(cell_name, '0'))
                subset.append(cell_value)
            except ValueError:
                subset.append(0)
        board.append(subset)
    
    incorrect_list = []
    for i in range(9):
        for j in range(9):
            if full_board[i][j] == board[i][j]:
                # print("Correct. Moving on.")
                continue
            else:
                if board[i][j] == 0 or board[i][j] == None:
                    # print("This square is empty. Moving on.")
                    continue
                else:
                    # print("Incorrect")
                    incorrect_list.append((bt_ss.row_idx(i), bt_ss.column_idx(i, j)))
    print(incorrect_list)
    if len(incorrect_list) > 0:
        flash("There are some incorrect squares. Try again! The incorrect squares are indicated red.", "error")

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                board[i][j] = None
    session['incorrect_list'] = incorrect_list
    return render_template("home.html", board=board, incorrect_list=incorrect_list)
    # return redirect("/")

@app.route("/clear", methods=['POST'])
def clearer():
    board = []

    for i in range(9):
        row = []
        for j in range(9):
            row.append(None)
        board.append(row)
    
    return render_template("solver.html", board=board)

@app.errorhandler(404)  # this is the check 404 error page
def not_found(e):
	return render_template("not_found.html")

if __name__ == "__main__":
    app.run(debug=True)