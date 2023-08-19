from flask_restful import reqparse
from database_connection import (
    connect_to_databse,
    hash_password,
    app,
    logging,
    cross_origin,
)


# initialize request parser that will be used in user creation
parser = reqparse.RequestParser()
parser.add_argument("userName", required=True)
parser.add_argument("password", required=True)
parser.add_argument("email")
parser.add_argument("mobileNumber")
parser.add_argument("address")
parser.add_argument("userType", required=True)


@app.route("/adduser", methods=["POST"])
@cross_origin()
def add_user():
    args = parser.parse_args()
    user_name = args["userName"]
    hashed_password = hash_password(args["password"])
    email = args["email"]
    mobile_number = args["mobileNumber"]
    address = args["address"]
    user_type = args["userType"]

    response_message = "False"

    connection = connect_to_databse()
    try:
        # run query
        cursor = connection.cursor()
        sql = f"""INSERT INTO users (user_name, password, email, mobile_number, address, user_type) 
                    Values ('{user_name}', "{hashed_password}", '{email}', '{mobile_number}', '{address}', '{user_type}')"""
        cursor.execute(sql)
        connection.commit()
        logging.debug("Query executed")
        logging.debug("User Created Successfully")
        response_message = "True"
    except Exception as e:
        logging.exception("Exception while executing query", str(e))
        if "UNIQUE constraint failed" in str(e.args):
            logging.debug("Username already exists")
        response_message = "False"
    finally:
        cursor.close()
        connection.close()
        return response_message
