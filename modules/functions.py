import re
import os

from modules import classes


def get_users():
    SIP_USERS_CONF = '/etc/asterisk/sip.conf'

    users = []
    fd = open(SIP_USERS_CONF, 'r')
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
            my_user = classes.User(username, fullname, callerid)
            # print(my_user)
            users.append(my_user)

    return users


def get_recordings(DATE):
    RECORDINGS_SOURCE_FOLDER = os.path.abspath(__file__ + "/../../") + "/data/recordings/"
    TARGET_FOLDER = RECORDINGS_SOURCE_FOLDER + DATE + "/"

    file_list = []
    for x in os.listdir(TARGET_FOLDER):
        file_list.append(x)

    record_list = []
    for fullname in file_list:
        TARGET_FOLDER_2 = TARGET_FOLDER + fullname + "/"
        # print(TARGET_FOLDER_2)

        file_list_2 = []
        for x in os.listdir(TARGET_FOLDER_2):
            file_list_2.append(x)

            TARGET_FOLDER_3 = TARGET_FOLDER_2 + x + "/"
            # print(TARGET_FOLDER_3)

            file_list_3 = []
            for x in os.listdir(TARGET_FOLDER_3):
                file_list_3.append(x)

                record = classes.Recording(x, TARGET_FOLDER_3)
                record_list.append(record)

    return record_list
