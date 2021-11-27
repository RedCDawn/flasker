# WIN
# export FLASK_ENV=development
# export FLASK_APP=hello.py
# MAC
# $env:FLASK_ENV = "development"
# $env:FLASK_APP = "hello"
from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)
# Create a route decorator
@app.route('/')

# def index():
#     return "<h1>hello world</h1>"

def index():
    first_name = "Chris"
    stuff = "this is some stuff"
    favorite_pizza = ["peperoni", "mozza", "calzone", "caprizioza", 41]

    return render_template("index.html", 
        first_name = first_name,
        favorite_pizza = favorite_pizza, 
        stuff = stuff)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", username=name)

# Create Custom Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

