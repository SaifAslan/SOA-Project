from flask import Flask
import logging
import sqlite3

app = Flask("UserLoginAPI")

# allow logging to include debug level messages
logging.basicConfig(level=logging.DEBUG)


def connect_to_databse():
    try:
        connection = sqlite3.connect("../database/soa_login")
    except Exception as e:
        logging.exception("Exception while connecting to database", str(e))
        return "Error occured while connecting to database"
    finally:
        return connection
