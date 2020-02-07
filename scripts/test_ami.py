# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

import json
from modules import functions


data = json.load(open('/home/whv/whv_ast_ms/security/access.json'))

HOSTNAME = str(data["ami"]["hostname"])
AMI_USER = str(data["ami"]["username"])
AMI_PASS = str(data["ami"]["password"])

print(HOSTNAME)
print(AMI_USER)
print(AMI_PASS)

ami_connector = functions.ast_ami_connect(HOSTNAME, AMI_USER, AMI_PASS)
print(ami_connector)

output = functions.ast_ami_run_command(ami_connector, "sip show peers")
print(output.response)


# for line in output.response:
#     print(line)
