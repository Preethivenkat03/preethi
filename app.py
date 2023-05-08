from flask import Flask, render_template, request

app = Flask


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Perform login validation here
    # You can check the credentials against the DB2 or any other authentication method
    if username == 'admin' and password == 'password':
        return 'Login Successful'
    else:
        return 'Login Failed'


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
