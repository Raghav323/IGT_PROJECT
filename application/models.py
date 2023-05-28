from flask import Flask
from flask_mongoengine import MongoEngine
from flask import current_app as app 



db = MongoEngine(app).markers

class Marker(db.Document):
    address = db.StringField(required=True)
    longitude = db.FloatField(required=True)
    latitude = db.FloatField(required=True)
