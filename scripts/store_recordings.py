"""
Gets recordings from /var/spool/asterisk/monitor/
and stores them in Django project (/static/recordings/) according to date (eg.201905)
"""
# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

import re
import os
import shutil

from modules import functions

RECORDINGS_SOURCE_FOLDER = "/var/spool/asterisk/monitor/"
# RECORDINGS_DEST_FOLDER = "/home/whv/whv_ast_ms/static/recordings/"
RECORDINGS_DEST_FOLDER = "/media/asterisk_recordings/"

file_list = []
try:
    for x in os.listdir(RECORDINGS_SOURCE_FOLDER):
        file_list.append(x)

    for filename in file_list:
        # print("\n\n\nFull filename = {}".format(RECORDINGS_SOURCE_FOLDER + filename))

        date = re.search(r'^(\d+)-', filename).group(1)
        short_date = re.search(r'^(\d{6})', date).group(1)
        # print(date)
        # print(short_date)

        wav_duration = functions.get_wav_duration(RECORDINGS_SOURCE_FOLDER + filename)
        # print("wav_duration = {}".format(wav_duration))

        if wav_duration > 5:
            # Copy all wav files larger than 5 seconds
            my_path = RECORDINGS_DEST_FOLDER + short_date + '/'
            try:
                os.makedirs(my_path)
            except FileExistsError:
                pass
            shutil.move(RECORDINGS_SOURCE_FOLDER + filename, my_path + filename)
        else:
            # Remove all wav filess shorter than 5 seconds
            os.remove(RECORDINGS_SOURCE_FOLDER + filename)
            pass

except Exception as Ex:
    print(Ex)