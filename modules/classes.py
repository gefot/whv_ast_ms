import re
from modules import functions

# USED BELOW WITHOUT THE VARIABLE
RECORDINGS_PATH = "/media/asterisk_recordings/"


####################################################################################
class AstUser:

    def __init__(self, username):
        self.username = username
        try:
            self.extension = re.match(r'(\d+)', username).group(1)
        except:
            self.extension = ""

        self.context = ""
        self.ip_address = ""
        self.port = ""
        self.useragent = ""
        self.reg_status = ""
        self.latency = ""

        self.first_name = ""
        self.last_name = ""
        self.callerid = ""
        self.email = ""
        self.mobile = ""

    def __str__(self):
        return "{} - {} {} - {} - {}".format(self.username, self.first_name, self.last_name, self.extension, self.callerid)

    def populate_peer_info(self, sip_peer_info):
        self.context = sip_peer_info['context']
        self.ip_address = sip_peer_info['ip_address']
        self.port = sip_peer_info['port']
        self.useragent = sip_peer_info['useragent']
        self.reg_status = sip_peer_info['reg_status']
        self.latency = sip_peer_info['latency']
        self.first_name = sip_peer_info['first_name']
        self.last_name = sip_peer_info['last_name']
        self.callerid = sip_peer_info['callerid']
        self.email = sip_peer_info['email']
        self.mobile = sip_peer_info['mobile']


####################################################################################
class User:

    def __init__(self, username, fullname, callerid):
        self.username = username
        self.fullname = fullname
        self.callerid = callerid
        try:
            self.firstname = re.search(r'^(\w+) ', fullname).group(1)
        except:
            self.firstname = ""
        try:
            self.lastname = re.search(r'^\w+ (\w+)', fullname).group(1)
        except:
            self.lastname = ""

    def __str__(self):
        return "{} - {} {} - {}".format(self.username, self.firstname, self.lastname, self.callerid)


####################################################################################
class Recording:

    def __init__(self, filename, fullpath):
        self.filename = filename
        self.fullpath = fullpath

        # THIS SHOULD BE RECORDINGS_PATH
        self.relative_path = re.search(r'/media/asterisk_recordings/(.*)', self.fullpath).group(1)
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
        return "{} - {} - {} - {} - {} - {} - {}".format(self.filename, self.fullpath, self.fullname, self.src, self.dst, self.call_type, self.relative_path)


####################################################################################
# class SMS:
#
#     def __init__(self, id, sms_from, sms_to, sms_text):
#         self.id = id
#         self.sms_from = sms_from
#         self.sms_to = sms_to
#         self.sms_text = sms_text
#
#     def __str__(self):
#         return "{} - {} - {] - {}".format(self.id, self.sms_from, self.sms_to, self.sms_text)
#
#
####################################################################################
