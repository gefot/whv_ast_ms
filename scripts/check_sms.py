# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

import tailer
import re

from modules import functions
from scripts import import_creds

SMS_FILE = '/var/log/apache2/error.log'

for line in tailer.tail(open(SMS_FILE), 10000):
    if "dumpio:trace7" in line and "data-HEAP" in line and "body" in line:
        print(line)
        try:
            pattern1 = r'\"id\": \"([\S]+)\"}'
            pattern2 = r'\[([\S\s]+)\] \[dumpio:trace7\]'
            pattern3 = r'\"from\": \"([\S]+)\", \"id\":'
            pattern4 = r'\"to\": \"([\S]+)\", \"from\":'
            pattern5 = r'\"body\": \"([\S\s]+)\", \"to\":'

            sms_id = re.search(pattern1, line).group(1)
            sms_date = re.search(pattern2, line).group(1)
            try:
                sms_from = re.search(pattern3, line).group(1)
            except:
                sms_from = ""
            sms_to = re.search(pattern4, line).group(1)
            sms_text = re.search(pattern5, line).group(1)
            print(sms_id)
            print(sms_date)
            print(sms_from)
            print(sms_to)
            print(sms_text)

            # Check at DB for this SMS
            db_conn = functions.db_connect(import_creds.DB_CREDS)
            cursor = db_conn.cursor()

            query = "select * from sms where sms_id = '{}' ".format(sms_id)
            result = functions.execute_db_query(cursor, query)
            print("result = {}\n".format(result))
            if len(result) == 0:
                query = "INSERT INTO sms (sms_id, sms_date, sms_from, sms_to, sms_text) VALUES (%s, %s, %s, %s, %s)"
                values = (sms_id, sms_date, sms_from, sms_to, sms_text)
                cursor.execute(query, values)
                db_conn.commit()

            else:
                print("Found: {}\n".format(sms_id))

            db_conn.close()

            pass
        except Exception as ex:
            print(ex)
