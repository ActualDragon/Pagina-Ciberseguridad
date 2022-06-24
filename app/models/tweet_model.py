from datetime import datetime
from sys import stderr

from flask import session

from app import app
import html


class tweet_model:

    def sanitizeTweet(self, tweet):
        tweet=tweet.to_dict()
        isThereTweet=False
        for key, value in tweet.items() :
            if key=="tweet":
                isThereTweet=True
        if not isThereTweet:
            print("\n\nNO HAY TWEET :(\n\n", file=stderr)
            tweet["tweet"]="Empty tweet."
        if tweet["tweet"]=="":
            tweet["tweet"]="Empty tweet."
        print("\n\n",tweet["tweet"], ": ", html.escape(tweet["tweet"]), "\n\n", file=stderr)
        tweet["tweet"]=html.escape(tweet["tweet"])
        return tweet

    def tweetMetadata(self):
        metadata = {
            "userID": session.get("id"),
            "username": session.get("username"),
            "name": session.get("nombre"),
        }
        print(metadata["userID"])
        if metadata["userID"] is None:
            return False
        return metadata

    # Función para registrar en la base de datos.
    def sendTweet(self, tweet):
        # Obtenemos información de usuario
        userInfo = self.tweetMetadata()

        # Verificamos que la variable de ID tenga contenido.
        if userInfo is False:
            print("No hay información del usuario para procesar el tweet.")
            return False, "Error en validación"

        # Obtenemos el momento en que se generó el tweet.
        tweetDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        tweet=html.escape(tweet)
        # Agregamos tweet a DB.
        valida, msg = app.firebaseManager.agregaTweet(tweet, userInfo, tweetDate)

        return valida, msg

    def modifyTweet(self, newTweet, id):
        metadata = self.tweetMetadata()
        oldTweet, msg = app.firebaseManager.getTweetByID(id)
        editDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        newTweet=html.escape(newTweet)
        valid, msg = app.firebaseManager.editarTweet(
            id, newTweet, editDate, oldTweet, metadata
        )

    def deleteTweet(self, id):
        metadata = self.tweetMetadata()
        oldTweet, msg = app.firebaseManager.getTweetByID(id)

        valid, msg = app.firebaseManager.eliminarTweet(id, oldTweet, metadata)

    def get_all(self):
        tweets, msg = app.firebaseManager.getAllTweets()

        if not tweets:
            print("Error no tweet data")
            return False, "No tweet data"
        tweetsRecibidos = []
        count = 0

        # "screenname", "username", "timestamp", "tweet", "id"
        for tweet in tweets:
            
            _id = tweet.id
            tweetDict = self.sanitizeTweet(tweet)
            newTweet = {
                "screenname": tweetDict["name"],
                "username": tweetDict["username"],
                "timestamp": tweetDict["fecha"],
                "tweet": tweetDict["tweet"],
                "id": _id,
            }
            print("\nSending: ", tweetDict["tweet"], " => ", count)
            tweetsRecibidos.append(newTweet)
        return tweetsRecibidos
