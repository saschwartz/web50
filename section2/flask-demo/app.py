from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/somehtml')
def some_html():
	return render_template('hello.html')

@app.route('/message')
def message():
	message = "Flask is great"
        return render_template('message.html', message=message)

@app.route('/table')
def table():
	people = [{'firstname': 'Bob', 'lastname': 'Smith', 'age': 27}, 
		{'firstname': 'Jane', 'lastname': 'Smith', 'age': 29}] 
	return render_template('table.html', people=people)

@app.route('/index')
def index(): 
	return render_template('index.html')
