from flask import Flask
from flask_cors import CORS, cross_origin
import logging
import sqlite3
import bcrypt

app = Flask("UsersAPI")
CORS(app, origins="*", methods="*", allow_headers=["Content-Type"])
app.config["CORS_HEADERS"] = "Content-Type"

# allow logging to include debug level messages
logging.basicConfig(level=logging.DEBUG)


def connect_to_databse():
    try:
        connection = sqlite3.connect("../database/soa_registration")
    except Exception as e:
        logging.exception("Exception while connecting to database", str(e))
        return "Error occured while connecting to database"
    finally:
        return connection


def hash_password(password):
    hash = ""
    try:
        if password:
            # convert password to byte array
            bytes = password.encode("utf-8")

            # generate the salt
            salt = bcrypt.gensalt()

            # hash the password
            hash = bcrypt.hashpw(bytes, salt)
    except Exception as e:
        logging.exception("Exception while hashing password", str(e))
    finally:
        return hash
