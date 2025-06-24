import flask
from flask import request, jsonify

# create a flask app object
app = flask.Flask(__name__)
#(creates a flask object, app refers to flask object. Flask is a server that users can connect to and ask for information) 

# tell the server to reload each time the code changes
app.config["DEBUG"] = True

# load student dictionaries 

# create a route to display our name
@app.route("/", methods=["GET"])
def index():
    return "<h1> My name is Jude this is my website </h1>"

# create 2 routes
# - return all student data
# - return students by major 

# run the application
app.run()





















