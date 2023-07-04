from flask_restful import reqparse

from database_connection import connect_to_databse, app, logging


# initialize request parser that will be used in user creation
parser = reqparse.RequestParser()
parser.add_argument("userName", required=True)
parser.add_argument("password", required=True)


@app.route("/registerusercredentials", methods=["POST"])
def register_user_credentials():
    args = parser.parse_args()
    user_name = args["userName"]
    password = args["password"]

    connection = connect_to_databse()
    try:
        # run query
        cursor = connection.cursor()
        sql = f"""INSERT INTO userscredentials (username, password) VALUES ('{user_name}', '{password}')"""
        cursor.execute(sql)
        connection.commit()
        logging.debug("Query executed")
        return "User credentials added successfully"
    except Exception as e:
        logging.exception("Exception while executing query", str(e))
        return "Error occured while adding user credentials"
    finally:
        cursor.close()
        connection.close()
