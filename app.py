from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_bolivia_key'

def check_winner(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columnas
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]
    for c in win_combinations:
        if board[c[0]] == board[c[1]] == board[c[2]] != "":
            return board[c[0]]
    if "" not in board:
        return "Empate"
    return None

@app.route('/')
def index():
    if 'board' not in session:
        session['board'] = [""] * 9
        session['turn'] = "X"
        session['winner'] = None
    return render_template('index.html', board=session['board'], turn=session['turn'], winner=session['winner'])

@app.route('/move/<int:pos>')
def move(pos):
    board = session.get('board')
    if board[pos] == "" and not session.get('winner'):
        board[pos] = session['turn']
        session['winner'] = check_winner(board)
        session['turn'] = "O" if session['turn'] == "X" else "X"
        session['board'] = board
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.pop('board', None)
    session.pop('turn', None)
    session.pop('winner', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)