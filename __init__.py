from flask import Flask, render_template, request, redirect

import backtrack_sudoku_solver
import board_generator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hahathisissosecretlol12345'

@app.route("/")  # this sets the route to this page
def home():
	return render_template("home.html")

@app.route("/solver", methods=['POST', 'GET'])  # this sets the route to this page
def solver():
    board = board_generator.gen_board()
    backtrack_sudoku_solver.print_board_debug(board_generator.format(board))
    return render_template("solver.html", board=board)

@app.route("/gen", methods=['POST'])
def generate():
    return redirect("/solver")

@app.route('/solve', methods=['POST', 'GET'])
def solve():
    # Retrieve the Sudoku board data from the form
    board = []
    for i in range(27):
        subset = []
        for j in range(3):
            cell_name = f'cell-{i}-{j}'
            try:
                cell_value = int(request.form.get(cell_name, '0'))
                if cell_value != 0:
                    subset.append([cell_value])
                else:
                    subset.append([])
            except ValueError:
                subset.append([])
        board.append(subset)
    
    backtrack_sudoku_solver.print_board_debug(board)
    # Call the Sudoku solver function to solve the board
    backtrack_sudoku_solver.solve(board)
    # backtrack_sudoku_solver.print_board(board)
    solved_board = backtrack_sudoku_solver.format_back(board)
    return render_template('solver.html', board=solved_board)

@app.errorhandler(404)  # this is the check 404 error page
def not_found(e):
	return render_template("not_found.html")

if __name__ == "__main__":
    app.run(debug=True)