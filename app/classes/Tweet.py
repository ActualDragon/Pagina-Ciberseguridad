from sys import stderr


class Tweet:
    def __init__(
            self, tweet, nombre, username, id, date
        ):
            self.username = username
            self.nombre = nombre
            self.date = date
            self.tweet = tweet