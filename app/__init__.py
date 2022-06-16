from re import template
from flask import Flask, session
from flask_session.__init__ import Session
from flask.sessions import SecureCookieSessionInterface
from app.classes import FireBaseManager
import secrets


secret= secrets.token_urlsafe(16)
app = Flask(__name__,
            static_url_path='', 
            static_folder='static')
app.secret_key = secret
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.session_cookie = SecureCookieSessionInterface().get_signing_serializer(app)
#Setupeamos nuesttro manejador de la bdd

app.firebaseManager = FireBaseManager.FireBaseManager()
from app import controller

