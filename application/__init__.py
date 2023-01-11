from flask import Flask

app = Flask(__name__)

# this has to be at the bottom so it does not circulate 
from application import routes
