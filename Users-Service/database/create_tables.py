import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

# connect to database
connection = sqlite3.connect("soa_registration")
logging.debug("Connected to database successfully")

# create users table
sql = """
CREATE TABLE users (
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_name TEXT NOT NULL,
password TEXT NOT NULL,
email TEXT,
mobile_number TEXT,
address TEXT,
user_type TEXT NOT NULL COLLATE NOCASE,
CONSTRAINT username_not_empty CHECK(user_name != ''),
CONSTRAINT username_unique UNIQUE(user_name),
CONSTRAINT password_not_empty CHECK(password != ''),
CONSTRAINT usertype_not_empty CHECK(user_type != ''),
CONSTRAINT usertype_value CHECK (LOWER(user_type)='buyer' OR LOWER(user_type)='seller')
)"""


connection.execute(sql)
logging.debug("users table created successfully!")
connection.close()
