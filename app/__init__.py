from flask import Flask
from flask_session.__init__ import Session
from flask.sessions import SecureCookieSessionInterface
from flask_session.__init__ import Session

from app.classes import FireBaseManager

secret = secrets.token_urlsafe(16)
app = Flask(__name__, static_url_path="", static_folder="static")
app.secret_key = secret
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.session_cookie = SecureCookieSessionInterface().get_signing_serializer(app)
#Setupeamos nuestro manejador de la bdd

app.firebaseManager = FireBaseManager.FireBaseManager()

