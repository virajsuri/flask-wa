from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    myName = "Viraj"
    return render_template('index.html', title='Home', myName=myName)


@app.route('/page1')
def page1():
    return render_template('page1.html', title='Page 1')
