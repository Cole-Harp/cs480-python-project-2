# A simple Web API implemented in Python using Flask

import json

from flask import Flask, Response, request

# define the Flask web application
app = Flask(__name__)

requestLog = []

courseList = {
    "cis121": {
        "name": "Introduction to Programming",
        "credits": 4,
        "gradeList": {
            "Flint": "A",
            "Lin": "A",

        }
    },
    "cis122": {
        "name": "Data Structures",
        "credits": 4
    },
    "cis223": {
        "name": "Algorithms",
        "credits": 4
    },
    "cis224": {
        "name": "Computer Architecture",
        "credits": 4
    },
    "cs301": {
        "name": "CS Core: Operating Systems",
        "credits": 2
    },
    "cs302": {
        "name": "CS Core: Software Engineering and Parallel Computing",
        "credits": 2
    },
    "cs303": {
        "name": "CS Core: Programming Languages",
        "credits": 2
    },
    "cs304": {
        "name": "CS Core: Databases and Information Security",
        "credits": 2
    },
    "cs306": {
        "name": "Network Architectures",
        "credits": 2
    },
    "cs308": {
        "name": "Applied Algorithms",
        "credits": 2
    },
    "cs391w": {
        "name": "Computer Science Project 1",
        "credits": 4
    },
    "cs392w": {
        "name": "Computer Science Project 2",
        "credits": 4
    },
    "cs491w": {
        "name": "Computer Science Capstone 1",
        "credits": 4
    },
    "cs492w": {
        "name": "Computer Science Capstone 2",
        "credits": 4
    },
    "cs480": {
        "name": "Topics in Software Engineering",
        "credits": 2
    },
    "cs495": {
        "name": "Computer Science Seminar",
        "credits": 1
    },
}


@app.get('/api/v1/course')
@app.get('/api/v2/course')
def get_all_courses():
    """REST method to get all courses as a list"""

    requestLog.append(f"GET /api/v1/course")

    # Generate a Flask response
    resp = Response()
    # Set the Content-Type header, to tell the caller that the response is in JSON format.
    resp.content_type = "application/json"
    # Set the data to a JSON representation of the courseList dictionary.
    resp.data = json.dumps(courseList)

    # Returning the response from here will cause Flask to send it back to the client.
    return resp


@app.get('/api/v1/course/<id>')
@app.get('/api/v2/course/<id>')
def get_course(id):
    """REST method to get one specific course"""

    requestLog.append(f"GET /api/v1/course/{id}")

    # Generate a Flask response
    resp = Response()
    # Set the Content-Type header, to tell the caller that the response is in JSON format.
    resp.content_type = "application/json"

    # Does the requested course exist in the list?
    if not exists(id):
        return Response("Course not found", 404)

    # Set the data to a JSON representation of the courseList dictionary.
    resp.data = json.dumps(courseList[id])

    # Returning the response from here will cause Flask to send it back to the client.
    return resp


@app.put('/api/v2/course/<id>')
@app.put('/api/v1/course/<id>')
def put_new_course(id):
    """Add a new course to the course database"""

    requestLog.append(
        f"PUT /api/v1/course/{id} | {'blank' if 'Authorization' not in request.headers else 'Auth:' + request.headers['Authorization']} >>>\n{request.get_data()}\n<<<")

    # Check authorization
    auth_result = check_auth(request)
    if not auth_result:
        return Response("Not authorized", 401)

    # A PUT request is for a *new* request.
    # If this item already exists in the database, that's an error.
    if exists(id):
        return Response("Record already exists", 400)

    # Validate and get input
    user_input = get_request_json(request, True)
    # If we got a response back (i.e. an error), just return it.
    if type(user_input) is Response:
        return user_input

    # Good to go!
    courseList[id] = user_input

    return Response("Created", 201)  # 201 = Created


@app.post('/api/v1/course/<id>')
@app.post('/api/v2/course/<id>')
def update_course(id):
    """Update data for a course in the course database"""

    requestLog.append(
        f"POST /api/v1/course/{id} | {'blank' if 'Authorization' not in request.headers else 'Auth:' + request.headers['Authorization']} >>>\n{request.get_data()}\n<<<")

    # Check authorization
    auth_result = check_auth(request)
    if not auth_result:
        return Response("Not authorized", 401)

    # A POST request is for an *existing* request.
    # If this item doesn't exist in the database, that's an error.
    if not exists(id):
        return Response("Record does not exist", 404)

    # Validate and get input
    user_input = get_request_json(request,
                                  False)  # allow "bad" JSON because we're going to look for each item individually.
    # If we got a response back (i.e. an error), just return it.
    if type(user_input) is Response:
        return user_input

    try:
        if 'name' in user_input and user_input['name'] is not None:
            courseList[id]['name'] = str(user_input['name'])
        if 'credits' in user_input and user_input['credits'] is not None:
            courseList[id]['credits'] = int(user_input['credits'])
    except Exception as e:
        return Response("Bad data in submission", 400)

    return Response("Updated", 202)  # 202 - "Accepted"


@app.delete('/api/v1/course/<id>')
@app.delete('/api/v2/course/<id>')
def delete_course(id):
    """Delete data for a course in the course database. Requires authorization!"""

    requestLog.append(
        f"DELETE /api/v1/course/{id} | {'blank' if 'Authorization' not in request.headers else 'Auth:' + request.headers['Authorization']}")

    # Check authorization
    auth_result = check_auth(request)
    if not auth_result:
        return Response("Not authorized", 401)

    # A POST request is for an *existing* request.
    # If this item doesn't exist in the database, that's an error.
    if not exists(id):
        return Response("Record does not exist", 404)

    del (courseList[id])
    return Response("Deleted", 202)


def check_auth(req):
    if 'Authorization' not in req.headers:
        return False
    if req.headers['Authorization'] == "Bearer thisisnotverysecure":
        return True
    return False


def get_request_json(req, validate=True):
    """ Convenience method to validate and get the JSON object submitted by the user """

    # Try to parse the user submission
    # If not possible return a 400 Bad Request.
    # try:
    r = request.get_json()
    # except Exception as e:
    #    return Response("JSON not found!",400)

    if validate:
        # Validate the JSON input
        if not validate_json(r):
            return Response("Invalid JSON data found", 400)

    return r


def exists(id):
    """Convenience method to test if an ID exists in the database"""
    return id in courseList.keys()


def validate_json(json_obj):
    if 'name' not in json_obj:
        return False
    if 'credits' not in json_obj:
        return False
    if type(json_obj['name']) is not str:
        return False
    if type(json_obj['credits']) is not int:
        return False
    # All test passed...
    return True


# Add this to the root level of the code
courseGrades = {
    "cs392w": {
        "Flint": "A",
        "Lin": "A",
        "Carlin": "B",
        "Von": "C",
    },
    "cs5000": {
        "Flint": "A",
        "Lin": "A",
        "Carlin": "B",
        "Von": "C",
    },
}


# Decorate this method with an appropriate VERSION 2 API path.

@app.put('/api/v2/course/grades/<id>/')
def put_grades(id):
    gradeList = get_request_json(request, False)
    """Store a list of student grades. gradeList is a dictionary with key = student ID and value = grade. For example: {"FlintMillion": 'B', "LinChase": 'A'}"""

    # Does the requested course exist in the list?
    if not exists(id):
        return Response("Course not found", 404)


    # Post the list of student grades
    courseGrades[id] = gradeList

    try:
        if 'name' in gradeList and gradeList['name'] is not None:
            courseList[id]['name'] = str(gradeList['name'])
        if 'grade' in gradeList and gradeList['credits'] is not None:
            courseList[id]['grade'] = str(gradeList['grade'])
    except Exception as e:
        return Response("Bad data in submission", 400)

    return Response("Updated", 202)  # 202 - "Accepted"


# Decorate this method with an appropriate VERSION 2 API path.
@app.get("/api/v2/grade/<id>/<student_id>")
def get_student_grade(id, student_id):
    """Get a student's grade in a course."""

    # Does the requested course exist in the list?
    if not exists(id):
        return Response("Course not found", 404)
    # And in the grades list?
    if id not in courseGrades.keys():
        return Response("Course not found", 404)

    # Does the student exist in the grade list?
    if student_id not in courseGrades[id]:
        return Response("Student not found", 404)

    # Return the student's grade
    return courseGrades[id][student_id]


# Support all of the version 1 API calls under version 2!
# You can do this by creating shims:
@app.get('/api/v2/course/<id>')
def get_course_v2(id):
    return get_course(id)


if __name__ == "__main__":
    # Start the Web application.
    # Using '0.0.0.0' as the address allows external clients (from outside your computer)
    #   to connect to the API.    try:
    app.run(host="0.0.0.0")
