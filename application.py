from flask import Flask, render_template, session
import os

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ttt')
def ttt():
    session.clear()
    if 'board' not in session:
        session['board'] = [[None for _ in range(3)] for _ in range(3)]
    print(f"Board: {session['board']}")
    return render_template('ttt.html')

if __name__ == '__main__':
    app.run(debug=True)
