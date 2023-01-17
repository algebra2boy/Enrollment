import os

class Config(object):
    # use the key to check the cookie
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    # setting up mongoDB databse 
    MONGODB_SETTINGS = {
                        "db": "UMass_Amherst_enrollment",
                        "host": "localhost",
                        "port": 27017,
                        "alias": "default",
                        }