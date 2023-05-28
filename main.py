import os
from flask import Flask
from application import config
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_restful import Api

def create_app():
    app = Flask(__name__, template_folder="templates")
    
    app.app_context().push()
    api = Api(app)
    return app,api

app ,api= create_app()
CORS(app)

DB_URI = "mongodb+srv://IGT_TEAM_2 :IGT_PASS_TEAM_2@IGT_MAP.mongodb.net/test?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI

# Import all the controllers so they are loaded

from application.api import * #Import all APIs
from application.controllers import *

# Special Pages

@app.errorhandler(404)
def page_not_found(e):
   return render_template("404.html")



if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',port=8080)
