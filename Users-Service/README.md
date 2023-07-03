This service uses Python Flask and REST to register users in an SQLite database. It contains 2 gateways; "/adduser" for user creation and "/getuser/<user_name>" for getting user details.

"/adduser" uses a POST method that requires a request containing the following fields:
1- userName (unique, not empty)
2- password (not empty)
3- email
4- mobileNumber
5- address
6- userType (not empty, "buyer" or "seller" case insensitive)

"/getuser/<user_name>" uses a GET method that requires the username and returns the user details from the database.

To run the app (should not be required as it should be covered by docker as per my understanding):
1- create python virtual environment (using command palete in vs code)
2- check requirements.txt file for required Flask and Flask-Restful modules (use "pip install" command)
3- navigate to the "api" folder
4- run "python -m flask run" in terminal