import os
from unittest import result
from urllib import response
import requests
import app 
import sqlite3
from dotenv import load_dotenv
from flask import Flask, request, json
from email_validator import validate_email, EmailNotValidError
load_dotenv() 

email_api=os.environ.get('email_api')
def is_email_valid(email):
    api_key = email_api
    email_address = email
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email_address},
        headers = {'Authorization': "Bearer " + api_key })
    status = response.json()['status']
    return response.json()['status']


