from flask import (Flask, request, render_template)
app = Flask(__name__)


@app.route('/')
def index():
    return 'Home Page'


@app.route('/users/<username>')
def recepie(username):
    return username


@app.route('/2018-W25', methods=['POST'])
def weekly_recepie():
    return request.form['recepie']


def login_user():
    return 'POST login'

def serve_login_page():
    return 'GET login'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_user()
    elif request.method == 'GET':
        return serve_login_page()


@app.route('/Shashank')
def name():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)
