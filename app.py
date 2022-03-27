from os import error
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from helpers import email
from flask_mail import Mail, Message

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT= 465,
    MAIL_USE_TLS= False,
    MAIL_USE_SSL= True,
    MAIL_USERNAME= 'cs50cat@gmail.com',
    MAIL_DEFAULT_SENDER= 'cs50cat@gmail.com'
    ))
mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/Cats", methods=["GET", "POST"])
def Cats():
    return render_template("cats.html")

@app.route("/Volunteer", methods=["Get", "POST"])
def Volunteer():
    return render_template("volunteer.html")

@app.route("/Contact", methods=["GET", "POST"])
def Contact():
    return render_template("contact.html")

@app.route("/About", methods=["GET", "POST"])
def About():
    return render_template("about.html")

@app.route("/Thanks", methods=["POST"])
def Thanks():
    return render_template("thanks.html")

@app.route("/Newsletter", methods=["POST"])
def newsletter():
    if request.method == "POST":
        status = email()
        if status == "error":
            flash("Please check your email", "warning")
            return render_template("index.html")
        if status == "valid":
            flash("Thank you for signing up!", "info")
            return render_template("index.html")
        else:
            flash("Invald email", "error")
            return render_template("index.html")