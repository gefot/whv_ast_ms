"""
This is a whv crontab; for every minute
"""

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
        print("\n")
        print(line)
        try:
            #
            # Search for SMS in logs
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
            # print(sms_id, sms_date, sms_from, sms_to, sms_text)

            #
            # Check at DB for this SMS
            db_conn = functions.db_connect(import_creds.DB_CREDS)
            cursor = db_conn.cursor()

            query = "select * from sms where sms_id = '{}' ".format(sms_id)
            result = functions.execute_db_query(cursor, query)

            #
            # If sms not found add DB
            if len(result) == 0:
                # Add SMS to DB
                query = "INSERT INTO sms (sms_id, sms_date, sms_from, sms_to, sms_text) VALUES (%s, %s, %s, %s, %s)"
                values = (sms_id, sms_date, sms_from, sms_to, sms_text)
                cursor.execute(query, values)
                db_conn.commit()

                # Find user e-mail and mobile for corresponding DID that SMS was sent to
                ami_connector = functions.ast_ami_connect(import_creds.AMI_CREDS)
                ast_users = functions.ast_ami_get_users(ami_connector)
                toaddr = ""
                for ast_user in ast_users:
                    if ast_user.callerid == sms_to:
                        toaddr = ast_user.email
                        if ast_user.mobile != "-" and ast_user.mobile != "":
                            mobile = ast_user.mobile
                        else:
                            mobile = ""

                # Send e-mail
                subject = "SMS from {} to {}".format(sms_from, sms_to)
                body = sms_text
                # toaddr = ["georgios.fotiadis@gmail.com"]
                toaddr = [toaddr]
                print(toaddr, subject, body)
                functions.send_mail(import_creds.EMAIL_CREDS['username'], import_creds.EMAIL_CREDS['password'], import_creds.EMAIL_CREDS['mail_server'], toaddr, subject, body, [],
                                    True, True)

                # TODO: Send SMS to mobile
                print(mobile)
            else:
                print("SMS already in DB: {}\n".format(sms_id))
            db_conn.close()

        except Exception as ex:
            print("No SMS found at error.log: {}".format(ex))
            continue
