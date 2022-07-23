from flask import (
    Blueprint,
    render_template,
    redirect,
    session,
    url_for
)

bp = Blueprint('ttt', __name__, url_prefix='/ttt')

# --------------------------------------------------------------------
#                             HELPER FUNCTIONS
# --------------------------------------------------------------------
def show(msg=''):
    print('*'*40)
    print(msg)
    print('*'*40)

def get_player():
    return session['turn']

def get_other_player():
    return 'O' if get_player()=='X' else 'X'

def toggle_turn():
    session['turn'] = get_other_player()

def row_check(row):
    other_player = get_other_player()
    if get_other_player() in session['board'][row] or None in session['board'][row]:
        return False
    return True

def col_check(col):
    other_player = get_other_player()
    for r in range(3):
        if other_player==session['board'][r][col] or None==session['board'][r][col]:
            return False
    return True

def is_winner_move(row, col):
    return row_check(row) or col_check(col)

def available_moves():
    moves = []
    for i in range(3):
        for j in range(3):
            if not session['board'][i][j]:
                moves.append((i, j))
    return moves

# --------------------------------------------------------------------
#                               ROUTES
# --------------------------------------------------------------------
@bp.route('/')
def game():
    if 'board' not in session:
        session['board'] = [[None for _ in range(3)] for _ in range(3)]
        session['turn'] = 'X'
        session['winner'] = None
        session['gameover'] = False

    show(f'Moves: {available_moves()}')

    return render_template('ttt.html', game={
        'board': session['board'],
        'turn': session['turn'],
        'winner': session['winner'],
        'gameover': session['gameover']
    })

@bp.route('/move/<int:row>/<int:col>')
def move(row, col):
    turn = get_player()
    session['board'][row][col] = turn
    
    if is_winner_move(row, col):
        session['winner'] = turn
    toggle_turn()
    return redirect(url_for('ttt.game'))

@bp.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('ttt.game'))
