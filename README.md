# Flask
Brushing up on flask configuration and REST API

## MongoDB setup
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/
```
$ brew tap mongodb/brew
$ brew update
$ brew install mongodb-community@6.0
```

## start MongoDB in the background
```
$ brew services start mongodb/brew/mongodb-community
$ mongosh
$ show dbs
```

## Set up
[Download MongoDB Compass](https://www.mongodb.com/try/download/compass)
[Flask configuration with MongoEngine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/flask_config.html)