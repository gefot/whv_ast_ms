import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/whv/whv_ast_ms/')

from app import app as application
application.secret_key = 'mysecretkey'