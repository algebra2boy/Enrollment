import os

class Config(object):
    # use the key to check the cookie
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    