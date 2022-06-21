from datetime import datetime
from sys import stderr

from flask import session

from app import app


class tweet_model:
    def tweetMetadata(self):
        metadata = {
            "userID": session.get("id") or "nqJOCtVKpSMMVyyBg6bHghbEIoa2",
            "username": session.get("username") or "joshua.haase",
            "name": session.get("name") or "Joshua",
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
        try:
            app.firebaseManager.agregaTweet(tweet, userInfo, tweetDate)
        except Exception as e:
            print("ERROR AGREGANDO TWEET\n\n:", str(e), file=stderr)
            return False
        return True
