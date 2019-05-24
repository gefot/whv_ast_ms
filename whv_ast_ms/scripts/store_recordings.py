import re
import os
import shutil

class User:
    def __init__(self, username, fullname, callerid):
        self.username = username
        self.fullaname = fullname
        self.callerid = callerid

    def __str__(self):
        return "{} - {} - {}".format(self.username, self.fullaname, self.callerid)


def get_users_from_sipconf(FILENAME):

    users = []

    fd = open(FILENAME, 'r')
    for line in fd:
        myline = line.strip()
        if myline.startswith("[1") and 'p' not in myline and '-' not in myline:
            username = re.search(r'\[(\d+)\]', myline).group(1)
            # print(username)
            next_line = next(fd)
            fullname = re.search(r'\"(.*)\"', next_line).group(1)
            # print(fullname)
            callerid = re.search(r'<(.*)>', next_line).group(1)
            # print(callerid)
            my_user = User(username, fullname, callerid)
            users.append(my_user)

    return users


# Main
SIP_USERS_CONF = '/etc/asterisk/sip.conf'
RECORD_FILE_FOLDER = "/var/spool/asterisk/monitor/"
BASE_DIR = '/var/www/html/recordings/'

asterisk_users = get_users_from_sipconf(SIP_USERS_CONF)
for user in asterisk_users:
    print(user)

file_list = []
for x in os.listdir(RECORD_FILE_FOLDER):
    file_list.append(x)

for filename in file_list:
    print(filename)
    date = re.search(r'^(\d+)-', filename).group(1)
    print(date)
    src_num = re.search(r'.*FROM\-(.*)-TO', filename).group(1)
    print(src_num)
    dst_num = re.search(r'.*-TO-(.*)\.wav', filename).group(1)
    print(dst_num)

    for user in asterisk_users:
        if user.callerid == src_num:
            print("Outgoing call from {}".format(user.fullaname))

            my_path = BASE_DIR + date + '/' + user.fullaname + '/' + 'outgoing/'
            try:
                os.makedirs(my_path)
            except FileExistsError:
                pass

            shutil.move(RECORD_FILE_FOLDER+filename, my_path+filename)

        elif user.username == dst_num:
            print("Incoming call from {}".format(user.fullaname))
            my_path = BASE_DIR + date + '/' + user.fullaname + '/' + 'incoming/'
            try:
                os.makedirs(my_path)
            except FileExistsError:
                pass

            shutil.move(RECORD_FILE_FOLDER+filename, my_path+filename)

    print("\n\n")

