import os

from datetime import timedelta


#加密key
secret_key = os.urandom(24)

#session 有效期
sess_time = timedelta(days=7)