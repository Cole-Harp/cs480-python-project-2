# Python API Exercise

Steps for Phase 3:

This is an *individual* exercise - every class member should post a submission.

This version of the API adds two more things: a DELETE method, and authorization requirements for POST, PUT and DELETE.

1. Run the new version of the API.
2. Try creating a PUT request to add a new course to the database:

        PUT /api/v1/course/<id>

    Note that you can't actually get a new course into the database because you are "Unauthorized" (code 401).

3. Now, try again, but this time go to the Auth tab in your request in Postman and set the token type to "JWT Bearer" and enter `thisisnotverysecure` as your bearer token. 

    > A **bearer token** is a token that gives permission to the *bearer* - that is, the person, program or service that knows it. If you know the bearer token, you are presumed to have all of the access that bearer token grants!

4. Finally, try making a `DELETE` request to *remove* an existing course in the database:
        
        DELETE /api/v1/course/<id>

    Then, use a `GET` request to ensure that your course has been deleted.

You should now have a `phase3.txt` file. Submit these two files to the "REST API Exercise" dropbox on D2L. 

You can now get into your group and prepare for Phase 4... `git checkout phase4`
