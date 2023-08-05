from flask_restful import reqparse
from flask import Flask
import json
import logging
import requests
import bcrypt


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
    user = {}
    try:
        response = requests.get(f"http://127.0.0.1:5000/getuser/{user_name}")
        user_details = json.loads(response.text)
        logging.debug(user_details)
        if user_details and check_password(password, user_details["password"]):
            user["userID"] = user_details["userID"]
            user["userName"] = user_details["userName"]
            user["email"] = user_details["email"]
            user["mobileNumber"] = user_details["mobileNumber"]
            user["address"] = user_details["address"]
            user["userType"] = user_details["userType"]
            logging.debug(f"{user_name} was authenticated successfully")
        else:
            logging.debug("Incorrect credentials")
    except Exception as e:
        logging.exception("Exception occured while checking user credentials", str(e))
    finally:
        return user


def check_password(receied_password, hashed_password):
    is_correct = ""
    try:
        if receied_password:
            # convert password to byte array
            bytes = receied_password.encode("utf-8")
            # convert hashed password to byte array as it can only be stored as a string representation of
            # byte array in database
            hashed_password = hashed_password[1:].replace("'", "").encode("utf-8")
            # check password
            is_correct = bcrypt.checkpw(bytes, hashed_password)
    except Exception as e:
        logging.exception("Exception while checking password", str(e))
    finally:
        return is_correct
