import json

from database_connection import connect_to_databse, app, sqlite3, logging


@app.route("/getuser/<user_name>", methods=["GET"])
def get_user(user_name):
    user = {}
    connection = connect_to_databse()
    try:
        # include columns in query result
        connection.row_factory = sqlite3.Row
        # run query
        cursor = connection.cursor()
        sql = f"""SELECT * FROM users WHERE username = '{user_name}'"""
        cursor.execute(sql)
        row = cursor.fetchone()
        logging.debug("Query executed")
        if not row:
            return "Incorrect Username"
        else:
            user["userName"] = row["username"]
            user["password"] = row["password"]
            user["email"] = row["email"]
            user["mobileNumber"] = row["mobilenumber"]
            user["address"] = row["address"]
            user["userType"] = row["usertype"]
    except Exception as e:
        logging.exception("Exception while executing query", str(e))
        return "Error occured while fetching user details"
    finally:
        cursor.close()
        connection.close()
        return user
