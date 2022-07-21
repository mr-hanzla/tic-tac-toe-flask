from flask import Flask, redirect, render_template, session, url_for
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def show(msg=''):
    print('*'*40)
    print(msg)
    print('*'*40)

def toggle_turn():
    turn = session['turn']
    session['turn'] = 'O' if turn=='X' else 'X'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ttt')
def ttt():
    if 'board' not in session:
        session['board'] = [[None for _ in range(3)] for _ in range(3)]
        session['turn'] = 'X'
    show(f" {session['board']}")
    return render_template('ttt.html', game={
        'board': session['board'],
        'turn': session['turn']
    })

@app.route('/move/<int:row>/<int:col>')
def move(row, col):
    turn = session['turn']
    show(f"Row: {row}, Col: {col}, Turn: {turn}")
    session['board'][row][col] = turn
    toggle_turn()
    return redirect(url_for('ttt'))

@app.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('ttt'))

if __name__ == '__main__':
    app.run(debug=True)
