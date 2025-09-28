from flask import Flask,render_template

#Create a flask instance
app = Flask(__name__)

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


