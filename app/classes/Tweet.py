from sys import stderr


class Tweet:
    def __init__(
            self, tweet, date, userID, name, username
        ):
        self.name = name
        self.username = username
        self.date = date
        self.tweet = tweet
        self.userID = userID