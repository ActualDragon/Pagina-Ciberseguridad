from flask import session

from app import app


class tweet_model:
    def tweetMetadata(self):
        metadata = {
            "userID": session.get("id") or "nqJOCtVKpSMMVyyBg6bHghbEIoa2",
            "username": session.get("username") or "joshua.haase",
            "name": session.get("name") or "Joshua"
        }
        print(metadata["userID"])
        if metadata["userID"] is None:
            return(False)
        return(metadata)
