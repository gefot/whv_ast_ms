# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

from modules import functions

print(functions.get_ip_info("155.207.228.165"))


