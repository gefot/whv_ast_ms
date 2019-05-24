import re
from modules import classes
SIP_USERS_CONF = '/etc/asterisk/sip.conf'


def get_users():

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

