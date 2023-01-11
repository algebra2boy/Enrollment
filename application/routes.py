from application import app
from flask import render_template # use to render html file 

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=True)

@app.route("/courses")
def courses():
    return render_template("index.html", login=True)

@app.route("/register")
def register():
    return render_template("index.html", login=True)

@app.route("/login")
def login():
    return render_template("index.html", login=True)