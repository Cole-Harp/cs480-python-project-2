# Python API Exercise

Steps for Phase 2:

This is an *individual* exercise - every class member should post a submission.

This version of the API adds two things: POST and PUT requests for adding items to the course list, and another GET method that allows the course ID to be provided.

1. Run the new version of the API.
2. In Postman, make a GET request that requests a specific course. For example:

        GET /api/v1/course/cs480

    Run this query using Postman and observe the result - you only get a single course, not a list of courses.

3. Try creating a PUT request to add a new course to the database:

        PUT /api/v1/course/<id>

    Give the course an ID of your choosing. 

    Your request should include a **body** in JSON format like this:

        {
            "name": "My Great Course",
            "credits": 8
        }
    
    You need to provide a name for the course as well as a number of credits. The API will validate this information for you - try entering some invalid information.

4. Finally, try making a `POST` request to *change* an existing course in the database:
        POST /api/v1/course/<id>

    Try providing *only* a course name or a number of credits.

You should have a file called `phase2.txt` in your program path. Save this file for upload to D2L after phase 3.

Move on to Phase 3 by checking out the `phase3` branch.