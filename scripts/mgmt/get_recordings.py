import re
import os
import shutil

from modules import functions, classes

# Main
RECORDINGS_SOURCE_FOLDER = os.path.abspath(__file__ + "/../../../") + "/data/recordings/"
# print(RECORDINGS_SOURCE_FOLDER)
DATE = "20190522"
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

            record = classes.Recording(x,TARGET_FOLDER_3)
            record_list.append(record)

for record in record_list:
    print(record)

