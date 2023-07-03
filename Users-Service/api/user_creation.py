from flask_restful import reqparse

from database_connection import connect_to_databse, app, logging


# initialize request parser that will be used in user creation
parser = reqparse.RequestParser()
parser.add_argument("userName", required=True)
parser.add_argument("password", required=True)
parser.add_argument("email")
parser.add_argument("mobileNumber")
parser.add_argument("address")
parser.add_argument("userType", required=True)


@app.route("/adduser", methods=["POST"])
def add_user():
    args = parser.parse_args()
    user_name = args["userName"]
    password = args["password"]
    email = args["email"]
    mobile_number = args["mobileNumber"]
    address = args["address"]
    user_type = args["userType"]

    connection = connect_to_databse()
    try:
        # run query
        cursor = connection.cursor()
        sql = f"""INSERT INTO users (username, password, email, mobilenumber, address, usertype) 
                    Values ('{user_name}', '{password}', '{email}', '{mobile_number}', '{address}', '{user_type}')"""
        cursor.execute(sql)
        connection.commit()
        logging.debug("Query executed")
        return "User Created Successfully"
    except Exception as e:
        logging.exception("Exception while executing query", str(e))
        if "UNIQUE constraint failed" in str(e.args):
            return "Username already exists"
        else:
            return "Error occured while creating user"
    finally:
        cursor.close()
        connection.close()
