import threading
import time
from re import T
from sys import stderr


class User:
    correo = ""
    nombre = ""
    id = ""
    username = ""

    idToken = ""
    refreshToken = ""
    expirySeconds = 0
    sessionStartTime = 0

    def __init__(
        self, email, nombre, id, username, idToken, refreshToken, expirySeconds
    ):
        self.correo = email
        self.nombre = nombre
        self.id = id
        self.username = username
        self.idToken = idToken
        self.refreshToken = refreshToken
        self.expirySeconds = expirySeconds
        self.sessionStartTime = time.time()

    def checkSession(self):
        currTime = time.time()
        elapsed = currTime - self.sessionStartTime
        if elapsed > self.expirySeconds:
            self.refreshTokenFunc()

    def logout(self):
        print("Logout", file=stderr)

    def refreshTokenFunc(self):
        user = self.authManager.refreshToken(self.refreshToken)
        # now we have a fresh token{
        user = {"idToken": "a", "refreshToken": "b"}

        self.idToken = user["idToken"]
        self.refreshToken = user["refreshToken"]
