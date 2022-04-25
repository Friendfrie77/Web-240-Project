import os
import requests
from flask import Flask, request
from flask_mail import Mail, Message
from email_validator import validate_email, EmailNotValidError

def is_email_valid():
    api_key = "2b108cae-8197-46b9-89af-68d87286c19c"
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
