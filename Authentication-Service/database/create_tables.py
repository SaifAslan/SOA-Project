import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

# connect to database
connection = sqlite3.connect("soa_login")
logging.debug("Connected to database successfully")

# create userscredentials table
sql = """
CREATE TABLE userscredentials (
username TEXT PRIMARY KEY,
password TEXT NOT NULL,
CONSTRAINT password_not_empty CHECK(password != '')
)"""


connection.execute(sql)
connection.commit()
logging.debug("userscredentials table created successfully!")
connection.close()
