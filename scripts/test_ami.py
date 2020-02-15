# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

from modules import functions
from scripts import import_creds

ami_connector = functions.ast_ami_connect(import_creds.AMI_CREDS)
ast_users = functions.ast_ami_sip_show_peers(ami_connector)
for ast_user in ast_users:
    print(ast_user)



