from flask import session

from app import app


class login_model:
    def loginUser(self, username, password):
        user, msg = app.firebaseManager.loginUsuario(username, password)
        if user:
            app.loggedUser = user
            self.startSession(user)
            return True, ""
        else:
            return False, msg

    def registerUser(self, nombre, correo, password, confirmaPassword, username):
        if password != confirmaPassword:
            return False
        user = app.firebaseManager.registraUsuario(nombre, correo, password, username)
        if user:
            return True
        else:
            return False

    def doesUserExist(self, username):
        return app.firebaseManager.getUsuarioByUsername(username)

    def startSession(self, user):
        session["id"] = user.id
        session["nombre"] = user.nombre
        session["correo"] = user.correo
        session["username"] = user.username
