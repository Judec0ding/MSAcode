from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests
#top line: flask modules

# make a Flask app
app = Flask(__name__)   #__name__ designates app.py as primary file for the app itself
app.config["DEBUG"] = True

# set secret key
app.config["SECRET_KEY"] = "your secret key"

"""
Function to request student data from the api
Input: url
Output: JSON student data
"""
def get_student_data(url:str):
    # make a request
    response = requests.get(url)

    # convert response format to JSON
    response_JSON = response.json()
    return response_JSON

# create a route for the website index/root. Will display all student data
@app.route('/', methods=['GET'])
def index():
    # make a request to the student data api
    url = 'http://127.0.0.1:5000/api/students/all'

    # get the student data
    student_data = get_student_data(url)
    return render_template('index.html')


# run the flask app
app.run(port="5001")