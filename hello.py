from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello,world</h1>"

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)