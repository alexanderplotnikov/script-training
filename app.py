import os
from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#define Tables for a database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    #image
    #audio

    #  def __repr__(self):
    #      return f"User('{self.username}', '{self.email}')"


@app.route("/")
def index():

    # if request.method = "POST":
    #     return "Logged in"
    # else:
    return render_template("admin.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    #User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        #Ensure username was submitted
        if not request.form.get("username"):
            return "Error"
        
        #Ensure password was submitted
        elif not request.form.get("password"):
            return "Error"
        
        print(username)
        #Query database for username
        #todo
        #Ensure username exists and password is correct
        # todo -setup database table of users

        #session["user_id"] = database query goes here

        return redirect("/")
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



    return render_template("login.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/add", methods=["GET", "POST"])
def add_program():
    return render_template("add_program.html")


if __name__ == "__main__":
    app.run(debug=True) 