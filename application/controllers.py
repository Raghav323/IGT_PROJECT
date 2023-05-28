from flask import Flask, request
from flask import render_template
from flask import current_app as app

@app.route("/", methods=["GET"])
def UserPage():
    return render_template("home.html")



