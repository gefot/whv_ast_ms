import re
import os
import shutil

from modules import functions

# Main
RECORDINGS_SOURCE_FOLDER = os.path.abspath(__file__ + "/../../../") + "/data/recordings/"
# print(RECORDINGS_SOURCE_FOLDER)
DATE = "20190521"
TARGET_FOLDER = RECORDINGS_SOURCE_FOLDER + DATE + "/"

asterisk_users = functions.get_users()

file_list = []
for x in os.listdir(TARGET_FOLDER):
    file_list.append(x)

for fullname in file_list:
    print(fullname)
    TARGET_FOLDER_2 = TARGET_FOLDER + fullname + "/"
    print(TARGET_FOLDER_2)

    file_list_2 = []
    for x in os.listdir(TARGET_FOLDER_2):
        file_list_2.append(x)
        print(x)



#     date = re.search(r'^(\d+)-', filename).group(1)
#     # print(date)
#     src_num = re.search(r'.*FROM\-(.*)-TO', filename).group(1)
#     # print(src_num)
#     dst_num = re.search(r'.*-TO-(.*)\.wav', filename).group(1)
#     # print(dst_num)
#
#     for user in asterisk_users:
#         if user.callerid == src_num:
#             print("Outgoing call from {}".format(user.fullaname))
#
#             MY_PATH = TARGET_DIR + date + '/' + user.fullaname + '/' + 'outgoing/'
#             print(MY_PATH)
#             try:
#                 os.makedirs(MY_PATH)
#             except FileExistsError:
#                 pass
#
#             shutil.move(RECORDINGS_SOURCE_FOLDER + filename, MY_PATH + filename)
#
#         elif user.username == dst_num:
#             print("Incoming call from {}".format(user.fullaname))
#             MY_PATH = TARGET_DIR + date + '/' + user.fullaname + '/' + 'outgoing/'
#             try:
#                 os.makedirs(MY_PATH)
#             except FileExistsError:
#                 pass
#
#             shutil.move(RECORDINGS_SOURCE_FOLDER + filename, MY_PATH + filename)
#
#     print("\n\n")
