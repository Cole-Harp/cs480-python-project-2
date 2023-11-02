# Python API Exercise

This is a very simple REST API implemented in Python and Flask. This example shows you just how easily you can create a REST API. This API implements a list of courses, and stores all data in RAM - each time you restart the app, the data is reset.

1. Create a **virtual environment**.

    python -m virtualenv venv

    If this command fails, you need to install the `virtualenv` module. Try `pip install virtualenv` or `pip3 install virtualenv`. If none of these are working come see me.

    You can alternatively use `conda` if you are more familiar with Anaconda:

        conda create -n api-exercise
        conda activate api-exercise

2. Install the requirements file.

    pip install -r requirements.txt

3. Run the API:

    python api.py

4. If you don't already have it, install [Postman](https://www.postman.com/downloads/). 

    > You do not need to create an account to use Postman, look for an option to skip account creation when you run it.

5. In Postman, create a GET request to get the list of courses from the REST API. The URL will be:

    http://localhost:5000/api/v1/course

6. Run the query and see your results - you just made a REST API request!

Move on to Phase 2 by checking out the `phase2` branch.