# Python API Exercise

Steps for Phase 4:

**Phase 4 is a GROUP project. Only one submission per group is required!**

You will now *update* the API so that it can support multiple versions.

This README contains the code you need to add to create a new method for a version 2 API. **You should also make sure that all current V1 API endpoints will still work when called under V2.** For example, `/api/v2/course/<id>` should still work exactly the same as it does when called with `/api/v1/course/<id>`. 

You will add the following code. *You can't just copy and paste it verbatim - you'll need to, at a minimum, add the decorator to make the methods endpoints!* You can decide the path to the actual endpoints.

    # Add this to the root level of the code
    courseGrades = {}

    # Decorate this method with an appropriate VERSION 2 API path.
    def put_grades(id):

        gradeList = get_request_json(request,False)
        """Store a list of student grades. gradeList is a dictionary with key = student ID and value = grade. For example: {"FlintMillion": 'B', "LinChase": 'A'}"""

        # Does the requested course exist in the list?
        if not exists(id):
            return Response("Course not found",404)
    
        # Post the list of student grades
        courseGrades[id] = gradeList

    # Decorate this method with an appropriate VERSION 2 API path.
    @app.get("/api/v2/grade/<id>/<student_id>")
    def get_student_grade(id, student_id):
        """Get a student's grade in a course."""

        # Does the requested course exist in the list?
        if not exists(id):
            return Response("Course not found",404)
        # And in the grades list?
        if id not in courseGrades.keys():
            return Response("Course not found",404)
        
        # Does the student exist in the grade list?
        if student_id not in courseGrades[id]:
            return Response("Student not found",404)

        # Return the student's grade
        return courseGrades[id][student_id]

    # Support all of the version 1 API calls under version 2!
    # You can do this by creating shims:
    @app.get('/api/v2/course/<id>')
    def get_course_v2(id):
        return get_course(id)
    
## Instructions

1. Add the new code to the API per the instructions.
2. **Test** your new API endpoints using Postman!
3. Submit your completed updated code to Dropbox. 
