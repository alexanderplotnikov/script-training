from flask import Flask
from flask import render_template, request
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

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


@app.route("/")
def login():

    # if request.method = "POST":
    #     return "Logged in"
    # else:
    return render_template("/login.html")
    
if __name__ == "__main__":
    app.run(debug=False) 