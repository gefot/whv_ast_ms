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
    def __init__(self, filename, fullpath):
        self.filename = filename
        self.fullpath = fullpath

        self.relative_path = re.search(r'/home/whv/whv_ast_ms/static/(.*)', self.fullpath).group(1)
        self.date = "unknown"
        self.time = "unknown"
        self.fullname = "unknown"
        self.src = "unknown"
        self.dst = "unknown"
        self.call_type = "unknown"
        self.wav_duration = "unknown"

        asterisk_users = functions.get_configured_users()

        try:
            date = re.search(r'^(\d+)-', filename).group(1)
            self.date = date
            self.date_gui = date[0:4] + "-" + date[4:6] + "-" + date[6:8]
        except:
            self.date = "unknown"
            self.date_gui = "unknown"

        try:
            time = re.search(r'^\d+-(\d+)-', filename).group(1)
            self.time = time
            self.time_gui = time[0:2] + ":" + time[2:4] + ":" + time[4:6]
        except:
            self.time = "unknown"
            self.time_gui = "unknown"
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
                # Replace source (10-digit number) with user fullname
                self.src = user.fullname
            elif user.username == self.dst:
                self.call_type = "incoming"
                self.fullname = user.fullname
                # Replace destination (4-digit  number) with user fullname
                self.dst = user.fullname

        wav_duration = functions.get_wav_duration(self.fullpath + filename)
        self.wav_duration = wav_duration

    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.filename, self.fullpath, self.fullname, self.src, self.dst, self.call_type)

####################################################################################
