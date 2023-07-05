from flask_restful import reqparse
from flask import Flask
import json
import logging
import requests


app = Flask("UserLoginAPI")

# allow logging to include debug level messages
logging.basicConfig(level=logging.DEBUG)

# initialize request parser that will be used in user creation
parser = reqparse.RequestParser()
parser.add_argument("userName", required=True)
parser.add_argument("password", required=True)


@app.route("/authenticateuser", methods=["POST"])
def authenticate_user():
    args = parser.parse_args()
    user_name = args["userName"]
    password = args["password"]
    return check_user_credentials(user_name, password)


def check_user_credentials(user_name, password):
    is_authenticated = "False"
    try:
        response = requests.get(f"http://127.0.0.1:5000/getuser/{user_name}")
        user_details = json.loads(response.text)
        logging.debug(user_details)
        if user_details and password == user_details["password"]:
            is_authenticated = "True"
            logging.debug(f"{user_name} was authenticated successfully")
        else:
            logging.debug("Incorrect credentials")
    except Exception as e:
        logging.exception("Exception occured while checking user credentials", str(e))
    finally:
        return is_authenticated
