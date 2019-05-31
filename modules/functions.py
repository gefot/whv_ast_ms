import re
import os
import subprocess

from modules import classes


####################################################################################
def get_users():
    """
    Traverses /etc/asterisk/sip.conf
    :return: list of User classes
    """
    SIP_USERS_CONF = '/etc/asterisk/sip.conf'

    users = []
    fd = open(SIP_USERS_CONF, 'r')
    for line in fd:
        myline = line.strip()
        if myline.startswith("[1") and 'p' not in myline and '-' not in myline:
            try:
                username = re.search(r'\[(\d+)\]', myline).group(1)
                next_line = next(fd)
                fullname = re.search(r'\"(.*)\"', next_line).group(1)
                callerid = re.search(r'<(.*)>', next_line).group(1)
                my_user = classes.User(username, fullname, callerid)
                # print(username)
                # print(fullname)
                # print(callerid)
                users.append(my_user)
            except:
                pass

    return users


####################################################################################
def get_recordings(date):
    """

    :param date: date to search for recording; in format 20190530
    :return: list of Recording classes
    """

    RECORDINGS_SOURCE_FOLDER = os.path.abspath(__file__ + "/../../") + "/static/recordings/"
    TARGET_FOLDER = RECORDINGS_SOURCE_FOLDER + date + "/"

    file_list = []
    record_list = []
    try:
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
    except:
        pass

    return record_list


####################################################################################
def get_wav_duration(wav_file):

    duration = subprocess.call(['soxi', '-D', wav_file])
    return duration


####################################################################################
