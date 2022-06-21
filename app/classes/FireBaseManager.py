from sys import stderr

import firebase_admin
import pyrebase
from firebase_admin import credentials, firestore

from app.classes import User
from requests.exceptions import HTTPError
import json


class FireBaseManager:
    firestoreManager = ""
    pyrebaseManager = ""

    def __init__(self):
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(
            cred, {"storageBucket": "seguridadproyecto-2a366.appspot.com"}
        )
        self.firestoreManager = firestore.client()
        config = {
            "apiKey": "AIzaSyAryxJPGDbzH8PmZKITRgB9y5wQWw69cNw",
            "authDomain": "seguridadproyecto-2a366.firebaseapp.com",
            "databaseURL": "https://seguridadproyecto-2a366-default-rtdb.firebaseio.com/",  # noqa E501
            "storageBucket": "seguridadproyecto-2a366.appspot.com",
            "serviceAccount": "credentials.json",
        }

        self.pyrebaseManager = pyrebase.initialize_app(config)

    def refreshToken(self, refreshT):
        auth = self.pyrebaseManager.auth()
        return auth.refresh(refreshT)

    def loginUsuario(self, mail, password):
        auth = self.pyrebaseManager.auth()
        try:
            user = auth.sign_in_with_email_and_password(mail, password)
            info = auth.get_account_info(user["idToken"])
            info = info["users"][0]
            print("INFO:", info, "\n\n\n", file=stderr)
            if not info["emailVerified"]:
                msg = "Usuario no verificado"
                print(msg, "\n\n\n", file=stderr)
                return False, msg
            datosUsuario = self.getUsuarioByID(user["localId"])
            myUser = User.User(
                user["email"],
                datosUsuario["nombre"],
                user["localId"],
                datosUsuario["usuario"],
                user["idToken"],
                user["refreshToken"],
                int(user["expiresIn"]),
            )
            print("USER:\n\n", myUser.correo, file=stderr)
            return myUser
        except HTTPError as e:
            print(
                "ERROR LOGIN\n\n:",
                json.loads(e.args[1])["error"]["message"],
                file=stderr,
            )
            return False, json.loads(e.args[1])["error"]["message"]

    def registraUsuario(self, nombre, mail, password, username):
        auth = self.pyrebaseManager.auth()
        existeUsuario = self.getUsuarioByUsername(username)
        if existeUsuario:
            print("ERROR REGISTRO, ya existe este usuario.\n\n:", file=stderr)
            return False
        try:
            user = auth.create_user_with_email_and_password(mail, password)
            auth.send_email_verification(user["idToken"])
            id = user["localId"]
            newValues = {
                "nombre": nombre,
                "email": mail,
                "UID": id,
                "usuario": username,
            }
            self.firestoreManager.collection("usuarios").document(id).set(newValues)
            myUser = User.User(
                mail, nombre, id, username, user["idToken"], user["refreshToken"], 3000
            )
            print("USER:\n\n", myUser.correo, file=stderr)
            return myUser
        except Exception as e:
            print("ERROR REGISTRO\n\n:", str(e), file=stderr)
            return False

    def getUsuarioByID(self, idUsuario):
        usuariosRef = self.firestoreManager.collection("usuarios")
        query = usuariosRef.where("UID", "==", idUsuario).get()
        if len(query) == 0:
            return False
        usuario = query[0].to_dict()
        return usuario

    def getUsuarioByUsername(self, username):
        usuariosRef = self.firestoreManager.collection("usuarios")
        query = usuariosRef.where("usuario", "==", username).get()
        if len(query) == 0:
            return False
        usuario = query[0].to_dict()
        return usuario

    def getUsuarios(self):
        usuarios = []
        usuariosQuery = self.firestoreManager.collection("usuarios").get()
        for usuario in usuariosQuery:
            usuarioDict = usuario.to_dict()
            usuarios.append(usuarioDict)
        return usuarios

    def getOtherUser(self):
        users = []
        usersQuery = self.firestoreManager.collection("usuarios").get()
        for user in usersQuery:
            userDict = user.to_dict()
            users.append(userDict)
        return users

    def getFollowingByID(self, idFollowing, idUsuario):
        following = self.getFollowingFromUsuario(idUsuario)
        print("FOLLOWING:\n\n", following, file=stderr)
        for user in following:
            if int(user["idNum"]) == int(idFollowing):
                print("FOLLOWING ENCONTRADO:\n\n", user, file=stderr)
                return user
        return False

    def getFollowingFromUsuario(self, idUsuario):
        following = []
        followingRef = (
            self.firestoreManager.collection("usuarios")
            .document(idUsuario)
            .collection("following")
            .get()
        )
        for uFollowing in followingRef:
            print("QUERIES:\n\n", uFollowing.to_dict(), file=stderr)
            followingDict = uFollowing.to_dict()
            following.append(followingDict)
        if len(following) == 0:
            return False
        return following

    def getFollowerByID(self, idFollower, idUsuario):
        follower = self.getFollowerFromUsuario(idUsuario)
        print("FOLLOWING:\n\n", follower, file=stderr)
        for user in follower:
            if int(user["idNum"]) == int(idFollower):
                print("FOLLOWER ENCONTRADO:\n\n", user, file=stderr)
                return user
        return False

    def getFollowerFromUsuario(self, idUsuario):
        followers = []
        followerRef = (
            self.firestoreManager.collection("usuarios")
            .document(idUsuario)
            .collection("followers")
            .get()
        )
        for follower in followerRef:
            print("QUERIES:\n\n", followerRef.to_dict(), file=stderr)
            followerDict = follower.to_dict()
            followers.append(followerDict)
        if len(followers) == 0:
            return False
        return followers

    def modificarTweet(self, id, nuevoTweet, date):
        tweetRef = (
            self.firestoreManager.collection("tweets").document(id)
        )
        if tweetRef is None:
            False
        # tweetRef.update("tweet": nuevoTweet, "date": date) ## Invalid syntax
        return True
        # query = tweetsRef.where("idNum", "==", int(idTweet)).get()
        # field_updates = {"contenido": nuevoTweet, "fecha": date}
        # for tweet in query:
        #     doc = tweetsRef.document(tweet.id)
        #     doc.update(field_updates)
        #     return True
        # return False

    def eliminarTweet(self, id):
        try:
            self.firestoreManager.collection("tweets").document(id).delete()
            return True
        except Exception as e:
            print("ERROR DELETE TWEET\n\n:", str(e), file=stderr)
            return False

    def agregaTweet(self, tweet, userInfo, date):
        newValues = {
            "userID": userInfo["userID"],
            "name": userInfo["name"],
            "username": userInfo["username"],
            "tweet": tweet,
            "fecha": date # dd/mm/YY H:M:S
        }
        self.firestoreManager.collection("tweets").document().set(newValues)

    def sendTweets(self):
        return self.firestoreManager.collection("tweets")
