# WIN
# export FLASK_ENV=development
# export FLASK_APP=hello.py
# MAC
# $env:FLASK_ENV = "development"
# $env:FLASK_APP = "hello"
from flask import Flask, render_template, flash

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"


# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

    # BooleanField
    # DateField
    # DateTimeField
    # DecimalField
    # FileField
    # HiddenField
    # MultipleField
    # FieldList
    # FloatField
    # FormField
    # IntegerField
    # PasswordField
    # RadioField
    # SelectField
    # SelectMultipleField
    # SubmitField
    # StringField
    # TextAreaField

    # # VALIDATORS
    # DataRequired
    # Email
    # EqualTo
    # InputRequired
    # IPAddress
    # Length
    # MacAddress
    # NumberRange
    # Optional
    # RegExp
    # URL
    # UUID
    # AnyOf
    # NoneOf



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

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully")
    return render_template("name.html", 
        name=name, 
        form=form)