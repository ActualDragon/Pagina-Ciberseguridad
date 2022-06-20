from sys import stderr


class Tweet:
    def __init__(
            self, tweet, date, userID
        ):
        self.date = date
        self.tweet = tweet
        self.id = id