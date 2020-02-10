# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

import json
from modules import functions

data = json.load(open('/home/whv/whv_ast_ms/security/access.json'))
ADDRESS = str(data["ami"]["address"])
AMI_USER = str(data["ami"]["username"])
AMI_PASS = str(data["ami"]["password"])

# ami_connector = functions.ast_ami_connect(ADDRESS, AMI_USER, AMI_PASS)
# ast_users = functions.ast_ami_sip_show_peers(ami_connector)
ast_users = functions.ast_get_sip_peers()

for ast_user in ast_users:
    print(ast_user)


