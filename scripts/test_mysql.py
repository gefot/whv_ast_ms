# This is needed so as to be run on CLI
import sys

sys.path.append('/home/whv/whv_ast_ms/')

from modules import functions
from scripts import import_creds

db_conn = functions.db_connect(import_creds.DB_CREDS)
cursor = db_conn.cursor()

query = "select * from cdr"
result = functions.execute_db_query(cursor, query)
for res in result:
    print(res)

query = "select * from sms ORDER BY sms_date"
result = functions.execute_db_query(cursor, query)
for res in result:
    print(res)

db_conn.close()
