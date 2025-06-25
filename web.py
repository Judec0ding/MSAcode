import flask
#flask allows us to build web applications with python
from flask import request, jsonify
import student_generator_v2 as sg


# create a flask app object
app = flask.Flask(__name__)
#(creates a flask object, app refers to flask object. Flask is a server that users can connect to and ask for information) 

# tell the server to reload each time the code changes
app.config['DEBUG'] = True

# load student dictionaries 

# create a route to display our name
@app.route('/', methods=['GET'])
# calling the app calls the function
def index():
    return '<h1> My name is Jude this is my website </h1>'

# create a route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    # load student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

# create a route to return students by major
@app.route('/api/majors/<string:major>', methods=['GET'])  #note: ' ' is the url. string:major is basically a variable which is input by user, such as english, mathematics (api/majors/english)
def api_students_by_major(major:str):
    # get students with major
    # get all students
    student_dictionaries = sg.get_student_dictionaries()
    major_students = []
    #use for loop to search
    for student in student_dictionaries:
        if major.lower() == student['major'].lower():
            major_students.append(student)

    return jsonify(major_students)




# create 2 routes
# - return all student data
# - return students by major 

# run the application
app.run()






















