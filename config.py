import os

class Config(object):
    # use the key to check the cookie
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xa4\x18\xca\xa2\x7f\xbe\x16\xec\xe5\x88*\x163M\xdd\xee'

    # setting up mongoDB databse 
    MONGODB_SETTINGS = {
                        "db": "UMass_Amherst_enrollment",
                        "host": "localhost",
                        "port": 27017,
                        "alias": "default",
                        }