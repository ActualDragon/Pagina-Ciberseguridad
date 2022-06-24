from datetime import datetime

from flask import session

from app import app


class tweet_model:
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

        # Agregamos tweet a DB.
        valida, msg = app.firebaseManager.agregaTweet(tweet, userInfo, tweetDate)

        return valida, msg

    def modifyTweet(self, newTweet, id):
        metadata = self.tweetMetadata()
        oldTweet, msg = app.firebaseManager.getTweetByID(id)
        editDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

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
            print(f"{tweet.to_dict()}")
            _id = tweet.id
            tweetDict = tweet.to_dict()
            if "tweet" in tweetDict:
                text=tweetDict["tweet"]
            else:
                text="Tweet vacío"
            newTweet = {
                "screenname": tweetDict["name"],
                "username": tweetDict["username"],
                "timestamp": tweetDict["fecha"],
                "tweet": text,
                "id": _id,
            }
            print("\nSending: ", tweetDict["tweet"], " => ", count)
            tweetsRecibidos.append(newTweet)
        return tweetsRecibidos
