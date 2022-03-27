import email_validator
import requests
from flask import Flask, request
from email_validator import validate_email, EmailNotValidError

def email():
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