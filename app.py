from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#Create a flask instance
app = Flask(__name__)

#csrf token #hide when uploading to github
app.config['SECRET_KEY'] = "my super secret key"

#add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#initilize the database
db = SQLAlchemy(app)

#Create a model


#Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("Whats your Name",validators=[DataRequired()])
    submit = SubmitField("Submit")
#Read about field and validators from flask Wtforms 

#Create a route decorator
@app.route('/')

#def index():
#    return "<h1>Hello World</h1>"

def index():
    return render_template("main.html")

# localhost:5000/user/pullak
@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name=name)

#Custom Error Page

#invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500



@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        #flash msg
        flash("Form Submitted Succesfully")

    return render_template('name.html',name = name,form = form)
