from re import T
from sys import stderr
import time, threading



class User:
    correo=""
    nombreCompleto=""
    id=""
    idToken=""
    refreshToken=""
    expirySeconds=0
    sessionStartTime=0
    authManager=""
    def __init__(self, email, nombre, id, idToken, refreshToken, expirySeconds, authManager):
        self.correo=email
        self.nombreCompleto=nombre
        self.id=id
        self.idToken=idToken
        self.refreshToken=refreshToken
        self.expirySeconds=expirySeconds
        self.authManager=authManager
        self.sessionStartTime=time.time()
    def checkSession(self):
        currTime=time.time()
        elapsed=currTime-self.sessionStartTime
        if(elapsed>self.expirySeconds): self.refreshTokenFunc()
    def logout(self):
        print("Logout", file=stderr)

        
    def refreshTokenFunc(self):
        user = self.authManager.refreshToken(self.refreshToken)
        # now we have a fresh token{
        user={"idToken":"a","refreshToken":"b"}

        self.idToken=user['idToken']
        self.refreshToken=user['refreshToken']