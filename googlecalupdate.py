from http import server
from sys import api_version
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)