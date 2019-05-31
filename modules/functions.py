import re
import os
import soundfile as sf

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

    RECORDINGS_SOURCE_FOLDER = "/home/whv/whv_ast_ms/static/recordings/"

    # Use short_date to search for recordings only to the corresponding month
    short_date = re.search(r'^(\d{6})', date).group(1)
    recordings_folder = RECORDINGS_SOURCE_FOLDER + short_date + "/"

    # Get user list from configuration
    asterisk_users = get_users()
    for user in asterisk_users:
        print(user)

    record_list = []
    try:
        for filename in os.listdir(recordings_folder):
            if filename.startswith(date):
                record = classes.Recording(filename, recordings_folder)
                record_list.append(record)
    except:
        pass

    return record_list


####################################################################################
def get_wav_duration(wav_file):

    f = sf.SoundFile(wav_file)
    samples = len(f)
    sampling_rate = f.samplerate
    duration = (int)(samples / sampling_rate)

    # print('samples = {}'.format(samples))
    # print('sample rate = {}'.format(sampling_rate))
    # print('seconds = {}'.format(duration))

    return duration

####################################################################################
