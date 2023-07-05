This service uses Python Flask and REST to authenticate users. It contains 1 gateway; "/authenticateuser" for user authentication.

"/authenticateuser" POST method:
input:
    userName (not empty)
    password (not empty)
output:
    "True"/"False"

To run the app (should not be required as it should be covered by docker as per my understanding):
1- create python virtual environment (using command palete in vs code)
2- check requirements.txt file for required Flask and Flask-Restful modules (use "pip install" command)
3- navigate to the "api" folder
4- run "python -m flask run -p 6000" in terminal