import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

# connect to database
connection = sqlite3.connect("soa_registration")
logging.debug("Connected to database successfully")

# create users table
sql = """
CREATE TABLE users (
username TEXT PRIMARY KEY,
password TEXT NOT NULL,
email TEXT,
mobilenumber TEXT,
address TEXT,
usertype TEXT NOT NULL COLLATE NOCASE,
CONSTRAINT password_not_empty CHECK(password != ''),
CONSTRAINT usertype_not_empty CHECK(usertype != ''),
CONSTRAINT usertype_value CHECK (LOWER(usertype)='buyer' OR LOWER(usertype)='seller')
)"""


connection.execute(sql)
logging.debug("users table created successfully!")
connection.close()
