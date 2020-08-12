from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World@'


    
@app.route('/<nomber>')
def greeting(nomber):
    return render_template('front.html', nomber=nomber)