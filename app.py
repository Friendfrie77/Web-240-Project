import os
from unittest import result
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from helpers import  is_email_valid
from flask_mail import Mail, Message
app = Flask(__name__, static_url_path='/static')
email= os.environ.get('email')
email_pass= os.environ.get('email_pass')
key= os.environ.get('app_key')
app.secret_key = 'key'
email= os.environ.get('email')
email_pass= os.environ.get('email_pass')
app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT= 465,
    MAIL_USE_TLS= False,
    MAIL_USE_SSL= True,
    MAIL_USERNAME= email,
    MAIL_PASSWORD= email_pass,
    MAIL_DEFAULT_SENDER= email

    ))
mail = Mail(app)
# for sending contact page messages #
def SendContactForm(result):
    msg=Message('Contact Form', recipients=["cs50cat@gmail.com"]) 
    msg.body= """
    Name: {}
    Email: {}
    Message: {}
    """.format(result['name'], result['email'], result ['message'])
    print(msg)
    mail.send(msg)
# start of html pages #
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
    if request.method == "POST":
        status = (request.form.get('email'))
        status = is_email_valid()
        if status == "error":
            flash("Please enter a vaild email adress!")
            return render_template("contact.html")
        else:
            result={}
            result['name'] = request.form.get('contact-name')
            result['email'] = request.form.get('email')
            result['message'] = request.form.get('message')

            SendContactForm(result)
            return render_template("contact.html")
    else:
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
        status = is_email_valid(request.form.get('email'))
        if status == "error":
            flash("Invaild email adresss!", "warning")
            return render_template("index.html")
        if status == "valid":
            flash("Thank you for signing up!", "info")
            return render_template("index.html")

