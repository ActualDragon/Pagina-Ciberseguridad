from hashlib import new
from pickle import TRUE
from app import app
from app.classes import User
from flask import Flask, session
from app import app
class login_model:
    def loginUser(self, username, password):
        user=app.firebaseManager.loginMedico(username, password)
        if user:
            app.loggedUser=user
            self.startSession(user)
            return True
        else:
            return False
    def registerUser(nombre,correo, password, confirmaPassword, username):
        if password!=confirmaPassword:
            return False
        user=app.firebaseManager.registraUsuario(nombre, correo, password, username)
        if user:
            return True
        else:
            return False

    def startSession(self, user):
        session["id"]=user.id
        session["nombre"]=user.nombreCompleto
        session["correo"]=user.correo

