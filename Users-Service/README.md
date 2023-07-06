This service uses Python Flask and REST to register users in an SQLite database. It contains 2 gateways; "/adduser" for user creation and "/getuser/<user_name>" for getting user details.

"/adduser" POST method:
input:
    userName (unique, not empty)
    password (not empty)
    email
    mobileNumber
    address
    userType (not empty, "buyer" or "seller" case insensitive)
output:
"True"/"False"


"/getuser/<user_name>" GET method:
input:
    userName
output:
    userID
    userName
    password
    email
    mobileNumber
    address
    userType ("buyer" or "seller")

To run the app (should not be required as it should be covered by docker as per my understanding):
1- create python virtual environment (using command palete in vs code)
2- check requirements.txt file for required Flask and Flask-Restful modules (use "pip install" command)
3- navigate to the "api" folder
4- run "python -m flask run -p 5000" in terminal