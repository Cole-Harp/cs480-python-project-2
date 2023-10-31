# A simple Web API implemented in Python using Flask

import json

from flask import Flask, Response, Request

# define the Flask web application
app = Flask(__name__)

courseList = {
    "cis121": {
        "name": "Introduction to Programming",
        "credits": 4
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
def get_all_courses():
    """REST method to get all courses as a list"""

    # Generate a Flask response
    resp = Response()
    # Set the Content-Type header, to tell the caller that the response is in JSON format.
    resp.content_type = "application/json"
    # Set the data to a JSON representation of the courseList dictionary.
    resp.data = json.dumps(courseList)

    # Returning the response from here will cause Flask to send it back to the client.
    return resp

if __name__ == "__main__":
    # Start the Web application.
    # Using '0.0.0.0' as the address allows external clients (from outside your computer) 
    #   to connect to the API.
    app.run(host="0.0.0.0")