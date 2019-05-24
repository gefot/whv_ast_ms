import re
import os
import shutil

from modules import functions

# Main
RECORD_FILE_FOLDER = "/var/spool/asterisk/monitor/"
BASE_DIR = '/var/www/html/recordings/'

asterisk_users = functions.get_users()
for user in asterisk_users:
    print(user)

file_list = []
print("lala")
for x in os.listdir(RECORD_FILE_FOLDER):
    file_list.append(x)

for filename in file_list:
    print(filename)
#     date = re.search(r'^(\d+)-', filename).group(1)
#     print(date)
#     src_num = re.search(r'.*FROM\-(.*)-TO', filename).group(1)
#     print(src_num)
#     dst_num = re.search(r'.*-TO-(.*)\.wav', filename).group(1)
#     print(dst_num)
#
#     for user in asterisk_users:
#         if user.callerid == src_num:
#             print("Outgoing call from {}".format(user.fullaname))
#
#             my_path = BASE_DIR + date + '/' + user.fullaname + '/' + 'outgoing/'
#             try:
#                 os.makedirs(my_path)
#             except FileExistsError:
#                 pass
#
#             shutil.move(RECORD_FILE_FOLDER+filename, my_path+filename)
#
#         elif user.username == dst_num:
#             print("Incoming call from {}".format(user.fullaname))
#             my_path = BASE_DIR + date + '/' + user.fullaname + '/' + 'incoming/'
#             try:
#                 os.makedirs(my_path)
#             except FileExistsError:
#                 pass
#
#             shutil.move(RECORD_FILE_FOLDER+filename, my_path+filename)
#
#     print("\n\n")
#
