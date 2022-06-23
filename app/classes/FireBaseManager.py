import json
from sys import stderr

import firebase_admin
import pyrebase
from firebase_admin import credentials, firestore
from requests.exceptions import HTTPError

from app.classes import User


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
            return myUser, "success"
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
        except HTTPError as e:
            print(
                "ERROR REGISTRO\n\n:",
                json.loads(e.args[1])["error"]["message"],
                file=stderr,
            )
            return False, json.loads(e.args[1])["error"]["message"]

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

    def editarTweet(self, id, nuevoTweet, date, oldTweet, metadata):
        print("\n\n\n", oldTweet, "\n\n\n", metadata, "\n\n\n", file=stderr)
        if oldTweet["userID"] != metadata["userID"]:
            return False, "Unvalid credentials"
        tweetRef = self.firestoreManager.collection("tweets").document(id)
        if tweetRef is None:
            False, "No existe tweet"
        args = {"tweet": nuevoTweet, "fecha": date}
        tweetRef.update(args)
        return True, "Success"

    def eliminarTweet(self, id, oldTweet, metadata):
        print("\n\n\n", oldTweet, "\n\n\n", metadata, "\n\n\n", file=stderr)
        if oldTweet is None:
            print("User data is None.")
            return False, "No data available for delete."
        if oldTweet["userID"] != metadata["userID"]:
            print("Tweet not available credentials.")
            return False, "Unvalid credentials"
        try:
            self.firestoreManager.collection("tweets").document(id).delete()
            print("Tweet deleted.")
            return True, "Success"
        except HTTPError as e:
            print(
                "ERROR EN DELETE\n\n:",
                json.loads(e.args[1])["error"]["message"],
                file=stderr,
            )
            return False, json.loads(e.args[1])["error"]["message"]

    def agregaTweet(self, tweet, userInfo, date):
        newValues = {
            "userID": userInfo["userID"],
            "name": userInfo["name"],
            "username": userInfo["username"],
            "tweet": tweet,
            "fecha": date,  # dd/mm/YY H:M:S
        }
        try:
            self.firestoreManager.collection("tweets").document().set(newValues)
            return True, "Success"
        except HTTPError as e:
            print(
                "ERROR AGREGAR TWEET:\n\n",
                json.loads(e.args[1])["error"]["message"],
                file=stderr,
            )
            return False, json.loads(e.args[1])["error"]["message"]

    def sendTweets(self):
        tweetList = []
        tweets = self.firestoreManager.collection("tweets").get()
        for tweet in tweets:
            tweetDict = tweet.to_dict()
            tweetList.append(tweetDict)
        return tweetList

    def getTweetByID(self, id):
        # Esto podría regresar un cursor (en nuestro caso no), puede ser el get().
        tweet = self.firestoreManager.collection("tweets").document(id).get()
        if tweet is None:
            return False, "None existing id."
        return tweet.to_dict(), "Success"

    def getAllTweets(self):
        tweets = self.firestoreManager.collection("tweets").stream()
        if not tweets:
            print("Error nothing to show")
            return False, "No tweets to show."
        print("Get all tweets from DB success.")
        return tweets, "Success"
