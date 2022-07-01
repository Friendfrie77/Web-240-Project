import os
from unittest import result
from urllib import response
import requests
import app 
import sqlite3
from dotenv import load_dotenv
from flask import Flask, request
from email_validator import validate_email, EmailNotValidError
load_dotenv() 

email_api=os.environ.get('email_api')
def is_email_valid(email):
    api_key = email_api
    email_address = request.form.get('email')
    try: 
        vaild=validate_email(email_address)
    except EmailNotValidError as e:
        status="error"
        return status
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
            params = {'email': email_address},
            headers = {'Authorization': "Bearer " + api_key })
    return response.json()['status']

def calinfo(jobID):
    jobinfo=[]
    jobs = sqlite3.connect("Site.db")
    cur= jobs.cursor()
    cur.execute("SELECT * FROM TJobs WHERE JobID = ?", jobID)
    result= cur.fetchall()
    for results in result:
        jobinfo.extend((results[1], results[5]))
    return jobinfo
