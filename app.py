import os
import sqlite3
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__, static_url_path='/static')
from helpers import is_email_valid

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
    msg=Message('Contact Form', recipients=[email]) 
    msg.body= """
    Name: {}
    Email: {}
    Subject: {}
    Message: {}
    """.format(result['name'], result['email'], result['subject'], result ['message'])
    mail.send(msg)
# if user wants a copy of message #
def UserContactForm(result):
    user_email=(result['email'])
    msg=Message('Your copy of contact message', recipients=[user_email])
    msg.body="""
    Hello,
    This is the copy of your contact message that you requested:
    Subject:{}
    Message:
    {}
    We will try to get back with you in 2-3 days.
    Thanks,
    Toebean Sanctuary
    """.format(result['subject'],result['message'])
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
    freejob = []
    day = []
    job = []
    jobs = sqlite3.connect("Site.db")
    cur = jobs.cursor()
    cur.execute('SELECT * FROM TDayJobs WHERE Taken = "0"')
    result = cur.fetchall()
    for results in result:
        day.append(results[1])
        freejob.append(results[2])
    cur.execute('SELECT * FROM TJobs')
    result = cur.fetchall()
    for results in result:
        job.append(results)
    jobs.close
    return render_template("volunteer.html", day=day, job=job)

@app.route("/Contact", methods=["GET", "POST"])
def Contact():
    if request.method == "POST":
        status = (request.form.get('email'))
        status = is_email_valid(status)
        check = (request.form.get('contact-check'));
        if status == "error":
            flash("Please enter a vaild email adress!")
            return render_template("contact.html")
        else:
            result={}
            result['name'] = request.form.get('contact-name')
            result['email'] = request.form.get('email')
            result['subject'] = request.form.get('subject')
            result['message'] = request.form.get('message')
            if check == "yes":
                UserContactForm(result)
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
        news_letter_email=request.form.get('email')
        status = is_email_valid(news_letter_email)
        if status == "error":
            flash("Invaild email adresss!", "warning")
            return render_template("index.html")
        if status == "valid":
            #sqlite connection to check if email is in db already.
            connection = sqlite3.connect("Site.db")
            cur = connection.cursor()
            result = cur.execute("SELECT NewsLetterPK FROM TNewsLetter WHERE STREmail='{email}'".format(email=news_letter_email))
            result = result.fetchone()
            if result is None:
                cur.execute("INSERT INTO TNewsLetter (StrEmail) VALUES ('{email}')".format(email=news_letter_email))
                connection.commit()
                connection.close()
                #sending newsletter
                print(news_letter_email)
                with app.open_resource("static/newsletters/newsletter.pdf") as fp:
                    msg=Message("Monthly News Letter", recipients=[news_letter_email])
                    msg.body="Here is this months newsletter"
                    msg.attach("newsletter.pdf", "application/pdf", fp.read())
                mail.send(msg)
                flash("Thank you for signing up!", "info")
                return render_template("index.html")
            else:
                flash("Looks like you are already signed up", "warning")
                return render_template("index.html")

       
