
class User:
    def __init__(self, username, fullname, callerid):
        self.username = username
        self.fullaname = fullname
        self.callerid = callerid

    def __str__(self):
        return "{} - {} - {}".format(self.username, self.fullaname, self.callerid)


