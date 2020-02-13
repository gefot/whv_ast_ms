import sys

sys.path.append('/home/whv/whv_ast_ms/')

import re
import os
import soundfile as sf

from modules import classes

import asterisk.manager
import pymysql as mariadb

SIP_USERS_CONF = '/etc/asterisk/sip.conf'
RECORDINGS_SOURCE_FOLDER = "/media/asterisk_recordings/"


####################################################################################
def ast_ami_connect(hostname, username, password):
    connector = asterisk.manager.Manager()
    # connect to the manager
    try:
        connector.connect(hostname)
        connector.login(username, password)

        # get connection status (returns Success is everything is ok)
        result = connector.status()
        # print(result)

        return connector

    except asterisk.manager.ManagerSocketException as ex:
        print("ast_ami_connect: Error in socket: {}".format(ex))
        raise Exception(ex)
    except asterisk.manager.ManagerAuthException as ex:
        print("ast_ami_connect: Error in auth: {}".format(ex))
        raise Exception(ex)
    except asterisk.manager.ManagerException as ex:
        print("ast_ami_connect: Error {}".format(ex))
        raise Exception(ex)


####################################################################################
def ast_ami_run_command(ami_connector, command):
    try:
        result = ami_connector.command(command)

        # Returns a list of lines with output of command
        return result.response

    except Exception as ex:
        print("ast_ami_run_command exception: ", ex)
        raise Exception(ex)


####################################################################################
def ast_ami_sip_show_peers(connector):
    try:
        ast_users = []
        command = "sip show peers"
        sip_peers = connector.command(command).response

        for sip_peer in sip_peers:
            try:
                sip_peer.strip('\n')
                sip_peer.strip('\r')
                my_peer = sip_peer.split()

                if 6 <= len(my_peer) <= 9 and my_peer[0] != "Name/username":
                    tmp_username = my_peer[0]
                    if re.search(r'/', tmp_username):
                        username = re.search(r'(\S+)\/', tmp_username).group(1)
                    else:
                        username = tmp_username

                    my_ast_user = classes.AstUser(username)
                    ast_users.append(my_ast_user)

            except Exception as ex:
                print("ast_ami_sip_peers - Error parsing user: ".format(ex))
                continue

        return ast_users

    except Exception as ex:
        print("ast_ami_sip_peers: {}".format(ex))
        raise Exception(ex)


####################################################################################
def ast_ami_sip_show_peer(connector, username):
    try:
        sip_peer_info = {}

        command = "sip show peer {}".format(username)
        # result = connector.command(command)
        my_sip_peer = connector.command(command).response

        for attr in my_sip_peer:
            try:
                attr_sublist = attr.split(':')
                if attr_sublist[0].strip() == "Context":
                    try:
                        sip_peer_info['context'] = attr_sublist[1].strip()
                    except:
                        sip_peer_info['context'] = ""
                elif attr_sublist[0].strip() == "Addr->IP":
                    try:
                        sip_peer_info['ip_address'] = attr_sublist[1].strip()
                        sip_peer_info['port'] = attr_sublist[2].strip()
                    except:
                        sip_peer_info['ip_address'] = ""
                        sip_peer_info['port'] = ""
                elif attr_sublist[0].strip() == "Useragent":
                    try:
                        sip_peer_info['useragent'] = re.search(r'(\S+)', attr_sublist[1]).group(1)
                    except:
                        sip_peer_info['useragent'] = ""
                elif attr_sublist[0].strip() == "Status":
                    try:
                        if "OK" in attr_sublist[1]:
                            sip_peer_info['reg_status'] = "registered"
                            latency = re.search(r'\S+\s\(([\S\s]+)\)', attr_sublist[1]).group(1)
                            sip_peer_info['latency'] = latency
                        elif "UNKNOWN" in attr_sublist[1]:
                            sip_peer_info['reg_status'] = "unregistered"
                            sip_peer_info['latency'] = ""
                        elif "LAGGED" in attr_sublist[1]:
                            sip_peer_info['reg_status'] = "lagged"
                            latency = re.search(r'\S+\s\(([\S\s]+)\)', attr_sublist[1]).group(1)
                            sip_peer_info['latency'] = latency
                    except:
                        sip_peer_info['reg_status'] = ""
                        sip_peer_info['latency'] = ""
                elif attr_sublist[0].strip() == "Callerid":
                    tmp = re.search(r'\"(\S+) (\S+)\" <\+(\d+)>', attr_sublist[1])
                    try:
                        sip_peer_info['first_name'] = tmp.group(1)
                    except:
                        sip_peer_info['first_name'] = ""
                    try:
                        sip_peer_info['last_name'] = tmp.group(2)
                    except:
                        sip_peer_info['last_name'] = ""
                    try:
                        sip_peer_info['callerid'] = tmp.group(3)
                    except:
                        sip_peer_info['callerid'] = ""

            except Exception as ex:
                print("ast_ami_sip_show_peer - Error parsing attribute: ".format(ex))
                continue

        return sip_peer_info

    except Exception as ex:
        print("ast_ami_sip_show_peer: {}".format(ex))
        raise Exception(ex)


####################################################################################
def get_configured_users():
    """
    Traverses /etc/asterisk/sip.conf
    :return: list of User classes
    """
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
            except Exception as Ex:
                print(Ex)

    return users


####################################################################################
def get_recordings(date):
    """

    :param date: date to search for recording; in format 20190530
    :return: list of Recording classes
    """

    record_list = []

    try:
        # Use short_date to search for recordings only to the corresponding month
        short_date = re.search(r'^(\d{6})', date).group(1)
        recordings_folder = RECORDINGS_SOURCE_FOLDER + short_date + "/"

        for filename in os.listdir(recordings_folder):
            try:
                if filename.startswith(date):
                    record = classes.Recording(filename, recordings_folder)
                    record_list.append(record)
            except Exception as Ex:
                print("In get_recordings: Exception:{} - {}".format(Ex, filename))
                pass

    except Exception as Ex:
        print(Ex)

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
def db_connect(db_creds):
    """
    :param db_creds: database credentials
    :return: database connector
    """

    # gfot: this is a rebase test

    try:
        conn = mariadb.connect(db_creds['db_host'], db_creds['db_username'], db_creds['db_password'], db_creds['db_name'])
        return conn

    except Exception as ex:
        print("db_connect exception: ", ex)
        raise Exception(ex)


####################################################################################
def execute_db_query(cursor, query):
    """
    :param cursor: database cursor
    :param query: database query
    :return: result
    """

    try:
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows

    except Exception as ex:
        print("execute_db_query exception: ", ex)
        raise Exception(ex)


####################################################################################
