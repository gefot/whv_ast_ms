import sys

sys.path.append('/home/whv/whv_ast_ms/')

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

my_password = "secret"

hashed_password = bcrypt.generate_password_hash(password=my_password)


print(hashed_password)