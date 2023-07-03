This service uses Python Flask and REST to authenticate users in an SQLite database. It contains 2 gateways; "/authenticateuser" for user authentication and "/registerusercredentials" for for saving user credentials.

"/authenticateuser" uses a POST method that requires a request containing the following fields:
1- userName (not empty)
2- password (not empty)

"/registerusercredentials" is used by the Users service and should not be used by the front end, it uses a POST method that requires a request containing the following fields:
1- userName (not empty)
2- password (not empty)

To run the app (should not be required as it should be covered by docker as per my understanding):
1- create python virtual environment (using command palete in vs code)
2- check requirements.txt file for required Flask and Flask-Restful modules (use "pip install" command)
3- navigate to the "api" folder
4- run "python -m flask run -p 6000" in terminal