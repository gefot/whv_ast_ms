# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

import json
from modules import functions

data = json.load(open('/home/whv/whv_ast_ms/security/access.json'))

DB_CREDS = {
    'db_host': str(data["asterisk-db"]["db_host"]),
    'db_username': str(data["asterisk-db"]["db_username"]),
    'db_password': str(data["asterisk-db"]["db_password"]),
    'db_name': str(data["asterisk-db"]["db_name"])
}

AMI_CREDS = {
    'address': str(data["ami"]["address"]),
    'username': str(data["ami"]["username"]),
    'password': str(data["ami"]["password"])

}
