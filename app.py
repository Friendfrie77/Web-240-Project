from enum import unique
import os
import sqlite3
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, flash
from flask_mail import Mail, Message
from sqlalchemy import ForeignKey, create_engine
app = Flask(__name__, static_url_path='/static')
from helpers import is_email_valid, calinfo
from flask_sqlalchemy import SQLAlchemy

load_dotenv() 
email= os.environ.get('email')
email_pass= os.environ.get('email_pass')
key= os.environ.get('app_key')
app.secret_key = 'key'
email= os.environ.get('email')
email_pass= os.environ.get('email_pass')
email_api=os.environ.get('email_api')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tddtipbsqhqrsr:b87452c7133c28fd4d34f433691dab174143cb898d245e451302dd6b19ca0b07@ec2-34-239-241-121.compute-1.amazonaws.com:5432/df1miji61o7lht'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///project.db'
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
db= SQLAlchemy(app)
engine = create_engine('postgresql://tddtipbsqhqrsr:b87452c7133c28fd4d34f433691dab174143cb898d245e451302dd6b19ca0b07@ec2-34-239-241-121.compute-1.amazonaws.com:5432/df1miji61o7lht')
print(engine.table_names())
#db model
class TNewsletter(db.Model):
    NesletterID = db.Column(db.Integer, primary_key=True)
    txtEmail= db.Column(db.String(200), nullable = False, unique = True )

    def __repr__(self):
        return '<Name %r>' % self.name
class TJobs(db.Model):
    JobsID = db.Column(db.Integer, primary_key=True)
    txtJobName = db.Column(db.String(200), nullable = False)
    txtJobdes = db.Column(db.String(6000), nullable = False)
    txtJobpic = db.Column(db.String(200), nullable = False)
    txtImgalt = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name

class TJobRes(db.Model):
    JobResID = db.Column(db.Integer, primary_key=True)
    JobID = db.Column(db.Integer, db.ForeignKey('TJobs.JobsID'), nullable=False)
    txtDate = db.Column(db.String(200), nullable=False)
    txtTime = db.Column(db.String(200), nullable=False)
    intPartySize = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


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
    job = []
    jobs_ID=[]
    for results in result:
        jobs_ID.append(results[0])
        job.append(results)
    jobs.close
    if request.method == "POST":
        count = 0
        partysize=int((request.form.get('party-size')))
        jobID= request.form.get('job-ID')
        txtCal= request.form.get('txtCal')
        txtTime= request.form.get('txtTime')
        jobs = sqlite3.connect("Site.db")
        cur = jobs.cursor()
        cur.execute("SELECT * FROM TDAYJOBS")
        result = cur.fetchall()
        count += partysize
        for number in jobs_ID:
            if int(jobID) == number:
                cur.execute("SELECT * FROM TDayJobs WHERE JobID=?", jobID)
                result= cur.fetchall()
                if (jobID != "2") or (jobID != "3"):
                    if count < 30:
                        for results in result:
                            if results[2] == txtCal:
                                count += results[4]
                        cur.execute("INSERT INTO TDayJobs (JobID, txtDate, txtTime, intPartySize) values (?,?,?,?)", (int(jobID), txtCal, txtTime, partysize))
                        jobs.commit()
                        jobs.close
                        jobinfo= calinfo(jobID)
                        return redirect('thanks.html')
                    else:
                        return redirect('volunteer.html', job=job)
                elif (jobID == "2") or (jobID == "3"):
                    if count < 10:
                        for results in result:
                            if results[2] == txtCal:
                                count =+ results[4]
                        cur.execute("INSERT INTO TDayJobs (JobID, txtDate, txtTime, intPartySize) values (?,?,?,?)", (int(jobID), txtCal, txtTime, partysize))
                        jobs.commit()
                        jobs.close
                else:
                    render_template("thanks.html")
        return render_template("volunteer.html", job=job)
    return render_template("volunteer.html", job=job)

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
            return redirect(request.referrer)
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
                return redirect(request.referrer)
            else:
                flash("Looks like you are already signed up", "warning")
                return redirect(request.referrer)

       
