from flask import Flask
from config import Config # a separate class to store the MongoDB settings
from flask_mongoengine import MongoEngine

db = MongoEngine() # initialize the mongoDB connection 
app = Flask(__name__)
app.config.from_object(Config) # retrieve all the mongo setting property from the Config class 

db.init_app(app) 

# this has to be at the bottom so it does not circulate 
from application import routes

