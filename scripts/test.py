# This is needed so as to be run on CLI
import sys
sys.path.append('/home/whv/whv_ast_ms/')

import datetime
from modules import functions
from scripts import import_creds


start = datetime.datetime.now()

# print(functions.get_ip_info("155.207.228.165"))
# print("\n--->Runtime = {} \n\n\n".format(datetime.datetime.now() - start))

ami_connector = functions.ast_ami_connect(import_creds.AMI_CREDS)
ast_users = functions.ast_ami_get_users(ami_connector)
for ast_user in ast_users:
    # print(ast_user)
    print(ast_user.__dict__)

# toaddr = ["georgios.fotiadis@gmail.com"]
# subject = "Test"
# body = "test"
# functions.send_mail(import_creds.EMAIL_CREDS['username'], import_creds.EMAIL_CREDS['password'], import_creds.EMAIL_CREDS['mail_server'], toaddr, subject, body, [], True, True)

print("\n--->Runtime = {} \n\n\n".format(datetime.datetime.now() - start))
