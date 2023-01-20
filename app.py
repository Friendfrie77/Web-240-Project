import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, flash, json, url_for, jsonify
from flask_mail import Mail, Message
from sqlalchemy import create_engine
import sqlalchemy
from flask_migrate import Migrate
app = Flask(__name__, static_url_path='/static')
from helpers import is_email_valid
from flask_sqlalchemy import SQLAlchemy
#env vars
load_dotenv() 
email= os.environ.get('email')
email_pass= os.environ.get('email_pass')
key= os.environ.get('app_key')
app.secret_key = 'key'
email= os.environ.get('email')
email_pass= os.environ.get('email_pass')
email_api=os.environ.get('email_api')
db_link = os.environ.get('db')
#setting up db connection
app.config['SQLALCHEMY_DATABASE_URI'] = db_link
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#setting up flask mail
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
migrate = Migrate(app, db)
#connecting to the db
engine = create_engine(db_link)  
# con = engine.connect()
#db model
class Useremail(db.Model):
    NewletterID = db.Column(db.Integer, primary_key=True)
    txtEmail= db.Column(db.String(200), nullable = False, unique = True )

class Jobs(db.Model):
    JobsID = db.Column(db.Integer, primary_key=True)
    txtJobName = db.Column(db.String(200), nullable = False)
    txtJobdes = db.Column(db.String(6000), nullable = False)
    txtJobpic = db.Column(db.String(200), nullable = False)
    txtImgalt = db.Column(db.String(200), nullable = False)
    volunteers = db.relationship('Jobopen', backref= 'jobs')
class Jobopen(db.Model):
    JobopenID = db.Column(db.Integer, primary_key=True, nullable=False)
    JobID = db.Column(db.Integer, db.ForeignKey('jobs.JobsID'), nullable=False)
    txtDate = db.Column(db.String(200), nullable=False)
    txtTime = db.Column(db.String(200), nullable=False)
    intPartySize = db.Column(db.Integer, nullable=False)
    jobocontact = db.relationship('JobContact', backref= 'jobopen')
class JobContact(db.Model):
    JobopenContactID = JobopenID = db.Column(db.Integer, primary_key=True, nullable=False)
    JobopenID = db.Column(db.Integer, db.ForeignKey('jobopen.JobopenID'), nullable=False)
    txtEmail= db.Column(db.String(200))
    txtName = db.Column(db.String(200), nullable = False)

class Cats(db.Model):
    CatsID = db.Column(db.Integer, primary_key=True, nullable=False)
    txtCatName = db.Column(db.String(200), nullable=False)
    txtCatGender = db.Column(db.String(200), nullable=False)
    txtCatAbout = db.Column(db.String(6000), nullable=False)
    txtCatImg = db.Column(db.String(200), nullable=False)

class Donationsimg(db.Model):
    DonationimgID = db.Column(db.Integer, primary_key=True, nullable=False)
    txtDontionimg = db.Column(db.String(200), nullable=False)
    txtAlt = db.Column(db.String(200), nullable=False)
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

#json apis
@app.route("/cal1")
def cal_1_info():
    try:
        jobinfo = open('static/json/data.json')
        jobinfo = json.load(jobinfo)
    except:
        pass
    cal_1=[]
    for dic in jobinfo:
        if dic['jobID'] == '1':
            cal_1.append(dic)
    return jsonify(cal_1)

@app.route("/cal2")
def cal_2_info():
    try:
        jobinfo = open('static/json/data.json')
        jobinfo = json.load(jobinfo)
    except:
        pass
    cal_2=[]
    for dic in jobinfo:
        if dic['jobID'] == '2':
            cal_2.append(dic)
    return jsonify(cal_2)

@app.route("/cal3")
def cal_3_info():
    try:
        jobinfo = open('static/json/data.json')
        jobinfo = json.load(jobinfo)
    except:
        pass
    cal_3=[]
    for dic in jobinfo:
        if dic['jobID'] == '3':
            cal_3.append(dic)
    return jsonify(cal_3)

@app.route("/cal4")
def cal_4_info():
    try:
        jobinfo = open('static/json/data.json')
        jobinfo = json.load(jobinfo)
    except:
        pass
    cal_4=[]
    for dic in jobinfo:
        if dic['jobID'] == '4':
            cal_4.append(dic)
    return jsonify(cal_4)

@app.route("/cal5")
def cal_5_info():
    try:
        jobinfo = open('static/json/data.json')
        jobinfo = json.load(jobinfo)
    except:
        pass
    cal_5=[]
    for dic in jobinfo:
        if dic['jobID'] == '5':
            cal_5.append(dic)
    return jsonify(cal_5)

@app.route("/cal6")
def cal_6_info():
    try:
        jobinfo = open('static/json/data.json')
        jobinfo = json.load(jobinfo)
    except:
        pass
    cal_6=[]
    for dic in jobinfo:
        if dic['jobID'] == '6':
            cal_6.append(dic)
    return jsonify(cal_6)

# start of html pages #
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/Cat", methods=["GET", "POST"])
def Cat():
    Adopt= []
    query = sqlalchemy.select(Cats)
    result = engine.execute(query).fetchall()
    for results in result:
        Adopt.append(results)
    print(Adopt)
    return render_template("cats.html", adopt=Adopt)

@app.route("/Volunteer", methods=["Get", "POST"])
def Volunteer():
    job = []
    jobs_ID=[]
    donoimg = []
    query= sqlalchemy.select(Jobs)
    result = engine.execute(query).fetchall()
    target = 0
    for results in result:
        jobs_ID.append(results[0])
        job.append(results)
    query = sqlalchemy.select(Jobopen).order_by(Jobopen.JobopenID.desc())
    result = engine.execute(query).fetchall()
    for results in result:
        target = results[0]
        break
    query =sqlalchemy.select(Donationsimg)
    result = engine.execute(query).fetchall()
    for results in result:
        donoimg.append(results)
    print(donoimg)
    #when users signs up for a job
    if request.method == "POST":
        count = 0
        itr = 0
        partysize=int((request.form.get('party-size')))
        jobID= request.form.get('job-ID')
        txtCal= request.form.get('txtCal')
        txtTime= request.form.get('txtTime')
        count += partysize
        check = (request.form.get('chkWavier'))
        # checks if user wants wavier *
        if check == 'on':
            txtEmail = request.form.get('txtEmail')
            status=is_email_valid(txtEmail)
            if (status == "error") or (status == "invalid"):
                    flash('Please enter a vaild email adress!', 'category2')
                    return render_template('volunteer.html', job=job, target=target)
            else:
                with app.open_resource("static/newsletters/newsletter.pdf") as fp:
                    msg=Message("Waiver", recipients=[txtEmail])
                    msg.body="Hello, this would be your wavier, but I did not feel comfortable sending a old wavier, or a fake one."
                    msg.attach("newsletter.pdf", "application/pdf", fp.read())
                mail.send(msg)
        #parses user data
        for number in jobs_ID:
            if int(jobID) == number:
                query = sqlalchemy.select(Jobopen).filter_by(JobID=jobID)
                result = engine.execute(query).fetchall() 
                if (jobID != "2") or (jobID != "3"):
                    for results in result:
                            if results[2] == txtCal:
                                count += results[4]
                    if count <= 30:
                        Job = Jobopen(JobID=jobID, txtDate=txtCal, txtTime=txtTime, intPartySize=partysize)
                        db.session.add(Job)
                        db.session.commit()
                    else:
                        flash('Sorry there are too many volunteers that day', 'category2')
                        return render_template ('volunteer.html', job=job, target=target)
                elif jobID == "2":
                    if count < 10:
                        for results in result:
                            if results[2] == txtCal:
                                count =+ results[4]
                        Job = Jobopen(JobID=jobID, txtDate=txtCal, txtTime=txtTime, intPartySize=partysize)
                        db.session.add(Job)
                        db.session.commit()
                    else:
                        flash('Sorry there are too many volunteers that day', 'category2')
                        return render_template('volunteer.html', job=job,target=target)
                #adding user contact info to db
                query = sqlalchemy.select(Jobopen).filter_by(JobID=jobID).order_by(Jobopen.JobopenID.desc())
                result = engine.execute(query).fetchall()
                JobopenID = 0
                for results in result:
                    JobopenID=results[0]
                    break
                if check == 'on':
                    user = JobContact(JobopenID=JobopenID, txtEmail = request.form.get('txtEmail'), txtName = request.form.get('txtName'))
                    db.session.add(user)
                    db.session.commit()
                else:
                    user = JobContact(JobopenID=JobopenID, txtEmail = 'Null', txtName = request.form.get('txtName'))
                    db.session.add(user)
                    db.session.commit()
                # setting up fullcalender data
                try:
                    jobinfo = open('static/json/data.json')
                    jobinfo = json.load(jobinfo)
                except:
                    jobinfo= []
                while itr != len(jobinfo):
                    for dic in jobinfo:
                        if (dic.get('jobID') == str(jobID)) and (dic.get('start')== txtCal):
                            jobinfo[itr]['title'] = F'Volunteers for the day {str(count)}'
                            itr += 1
                            jsonsave = open('static/json/data.json', 'w')
                            json.dump(jobinfo, jsonsave)
                            jsonsave.close()
                            return redirect(url_for('Thanks'))
                        else:
                            itr += 1
                else:
                    jobinfo.append({"jobID":jobID, "title":F'Volunteers for the day {str(partysize)}', "start":txtCal})
                    jsonsave = open('static/json/data.json', 'w')
                    json.dump(jobinfo, jsonsave)
                    jsonsave.close()
                    return redirect(url_for('Thanks'))
    return render_template("volunteer.html", job=job, target=target, donoimg = donoimg)

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

@app.route("/Thanks", methods=["Get","POST"])
def Thanks():
    return render_template("thanks.html")

@app.route("/Newsletter", methods=["POST"])
def newsletter():
    if request.method == "POST":
        news_letter_email=request.form.get('email')
        status = is_email_valid(news_letter_email)
        if (status == "error") or (status == "invalid"):
            flash("Invaild email adresss!", 'category1')
            return redirect(request.referrer)
        if status == "valid":
            user = Useremail.query.filter_by(txtEmail=news_letter_email).first()
            if user is None:
                user= Useremail(txtEmail=news_letter_email)
                db.session.add(user)
                db.session.commit()
                with app.open_resource("static/newsletters/newsletter.pdf") as fp:
                    msg=Message("Monthly News Letter", recipients=[news_letter_email])
                    msg.body="Here is this months newsletter"
                    msg.attach("newsletter.pdf", "application/pdf", fp.read())
                mail.send(msg)
                flash("Thank you for signing up!", 'category1')
                return redirect(request.referrer)
            else:
                flash("Looks like you are already signed up", 'category1')
                return redirect(request.referrer)

       