from flask import Flask, redirect, render_template, session, url_for
import os
import db
import tictactoe

# --------------------------------------------------------------
# app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

with app.app_context():
    db.init_app(app)
    db.init_db()

app.register_blueprint(tictactoe.bp)

# --------------------------------------------------------------
def show(msg=''):
    print('*'*40)
    print(msg)
    print('*'*40)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)
