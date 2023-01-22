from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    user_id     = db.IntField(unique=True)
    first_name  = db.StringField(max_length = 50)
    last_name   = db.StringField(max_length = 50)
    email       = db.StringField(unique=True, max_length = 30)
    password    = db.StringField()

    def set_hash_password(self, password):
        # password is always hashed no matter what
        # cannot store actual password in the database
        self.password = generate_password_hash(password=password)

    def get_hash_password(self, password):
        return check_password_hash(self.password, password)

class Course(db.Document):
    courseID      = db.StringField(unique=True, max_length = 10)
    title         = db.StringField(max_length = 150)
    description   = db.StringField(max_length = 250)
    credits       = db.IntField()
    term          = db.StringField(max_length = 30)

class Enrollment(db.Document):
    user_id       = db.IntField()
    courseID      = db.StringField(max_length = 10)
