
import re
from modules import functions


####################################################################################
class User:
    def __init__(self, username, fullname, callerid):
        self.username = username
        self.fullname = fullname
        self.callerid = callerid

        try:
            self.firstname = re.search(r'^(\w+) ', fullname).group(1)
            self.lastname = re.search(r'^\w+ (\w+)', fullname).group(1)
        except:
            self.firstname = "unknown"
            self.lastname = "unknown"

    def __str__(self):
        return "{} - {} {} - {}".format(self.username, self.firstname, self.lastname, self.callerid)


####################################################################################
class Recording:
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path

        self.relative_path = re.search(r'/home/whv/whv_ast_ms/static/(.*)', self.path).group(1)
        self.date = "unknown"
        self.time = "unknown"
        self.fullname = "unknown"
        self.src = "unknown"
        self.dst = "unknown"
        self.call_type = "unknown"

        asterisk_users = functions.get_users()

        try:
            date = re.search(r'^(\d+)-', filename).group(1)
            self.date = date
        except:
            self.date = "unknown"

        try:
            time = re.search(r'^\d+-(\d+)-', filename).group(1)
            self.time = time
        except:
            self.time = "unknown"
        try:
            src = re.search(r'.*FROM\-(.*)-TO', filename).group(1)
            self.src = src
        except:
            self.src = "unknown"

        try:
            dst = re.search(r'.*-TO-(.*)\.wav', filename).group(1)
            self.dst = dst
        except:
            self.dst = "unknown"

        for user in asterisk_users:
            if user.callerid == self.src:
                self.call_type = "outgoing"
                self.fullname = user.fullname
            elif user.username == self.dst:
                self.call_type = "incoming"
                self.fullname = user.fullname

    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.filename, self.path, self.fullname, self.src, self.dst, self.call_type)


####################################################################################
