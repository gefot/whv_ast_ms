# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

from modules import functions
from scripts import import_creds

ami_connector = functions.ast_ami_connect(import_creds.AMI_CREDS)
# ami_connector = functions.ast_ami_connect(ADDRESS, AMI_USER, AMI_PASS)
# ast_users = functions.ast_ami_sip_show_peers(ami_connector)
ast_users = functions.ast_get_sip_peers()

for ast_user in ast_users:
    print(ast_user)


