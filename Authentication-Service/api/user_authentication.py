from flask_restful import reqparse

from database_connection import connect_to_databse, app, logging


# initialize request parser that will be used in user creation
parser = reqparse.RequestParser()
parser.add_argument("userName", required=True)
parser.add_argument("password", required=True)


@app.route("/authenticateuser", methods=["POST"])
def authenticate_user():
    args = parser.parse_args()
    user_name = args["userName"]
    password = args["password"]

    connection = connect_to_databse()
    try:
        # run query
        cursor = connection.cursor()
        sql = f"""SELECT * FROM userscredentials WHERE username = '{user_name}' AND password = '{password}'"""
        cursor.execute(sql)
        row = cursor.fetchall()
        logging.debug("Query executed")
        if not row:
            return "Incorrect User Credentials"
        else:
            return row
    except Exception as e:
        logging.exception("Exception while executing query", str(e))
        return "Error occured while authenticating user"
    finally:
        cursor.close()
        connection.close()
