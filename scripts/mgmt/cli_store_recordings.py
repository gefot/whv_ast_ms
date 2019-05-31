"""
Gets recordings from /var/spool/asterisk/monitor/ and stores them in Django project (/static/recordings/)
using the appropriate structure (date/user/in-outgoing)
"""
# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

import re
import os
import shutil
import time

from modules import functions

# Main
RECORDINGS_SOURCE_FOLDER = "/var/spool/asterisk/monitor/"
TARGET_DIR = os.path.abspath(__file__ + "/../../../") + "/static/recordings/"
print(TARGET_DIR)

# Get user list from configuration
asterisk_users = functions.get_users()
for user in asterisk_users:
    print(user)

file_list = []
for x in os.listdir(RECORDINGS_SOURCE_FOLDER):
    file_list.append(x)

for filename in file_list:
    date = re.search(r'^(\d+)-', filename).group(1)
    src_num = re.search(r'.*FROM\-(.*)-TO', filename).group(1)
    dst_num = re.search(r'.*-TO-(.*)\.wav', filename).group(1)
    print(filename)
    # print(date)
    # print(src_num)
    # print(dst_num)

    short_date = re.search(r'^(\d{6})', date).group(1)
    # print(short_date)

    MY_PATH = TARGET_DIR + short_date + '/'
    try:
        os.makedirs(MY_PATH)
    except FileExistsError:
        pass

    shutil.move(RECORDINGS_SOURCE_FOLDER + filename, MY_PATH + filename)


#     for user in asterisk_users:
#         if user.callerid == src_num:
#             print("Outgoing call from {}".format(user.fullname))
#
#             MY_PATH = TARGET_DIR + date + '/' + user.firstname + user.lastname + '/' + 'outgoing/'
#             print(MY_PATH)
#             try:
#                 os.makedirs(MY_PATH)
#             except FileExistsError:
#                 pass
#
#             shutil.move(RECORDINGS_SOURCE_FOLDER + filename, MY_PATH + filename)
#
#         elif user.username == dst_num:
#             print("Incoming call from {}".format(user.fullname))
#             MY_PATH = TARGET_DIR + date + '/' + user.firstname + user.lastname + '/' + 'incoming/'
#             try:
#                 os.makedirs(MY_PATH)
#             except FileExistsError:
#                 pass
#
#             shutil.move(RECORDINGS_SOURCE_FOLDER + filename, MY_PATH + filename)
#             time.sleep(2)
#
#     print("\n\n")
