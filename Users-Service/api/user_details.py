from flask_restful import reqparse
from database_connection import (
    connect_to_databse,
    app,
    bcrypt,
    sqlite3,
    logging,
    cross_origin,
)


# initialize request parser that will be used in user creation
parser = reqparse.RequestParser()
parser.add_argument("userName", required=True)
parser.add_argument("password", required=True)


@app.route("/authenticateuser", methods=["POST"])
@cross_origin()
def authenticate_user():
    args = parser.parse_args()
    user_name = args["userName"]
    password = args["password"]
    return check_user_credentials(user_name, password)


def check_user_credentials(user_name, password):
    user = {}
    connection = connect_to_databse()
    is_error = False
    try:
        # include columns in query result
        connection.row_factory = sqlite3.Row
        # run query
        cursor = connection.cursor()
        sql = f"""SELECT * FROM users WHERE user_name = '{user_name}'"""
        cursor.execute(sql)
        row = cursor.fetchone()
        logging.debug("Query executed")
        if row is None:
            is_error = True
        else:
            user["password"] = row["password"]
            if check_password(password, user["password"]):
                user["userID"] = row["user_id"]
                user["userName"] = row["user_name"]
                user["email"] = row["email"]
                user["mobileNumber"] = row["mobile_number"]
                user["address"] = row["address"]
                user["userType"] = row["user_type"]
                logging.debug(f"{user_name} was authenticated successfully")
            else:
                is_error = True
    except Exception as e:
        logging.exception("Exception occured while checking user credentials", str(e))
        return f"Error occured while authenticating user {e}"
    finally:
        return user if not is_error else "Incorrect Credentials"


def check_password(receied_password, hashed_password):
    is_correct = ""
    try:
        if receied_password:
            # convert password to byte array
            bytes = receied_password.encode("utf-8")
            # convert hashed password to byte array as it can only be stored as a string representation of
            # byte array in database
            hashed_password = hashed_password[1:].replace("'", "").encode("utf-8")
            # check password
            is_correct = bcrypt.checkpw(bytes, hashed_password)
    except Exception as e:
        logging.exception("Exception while checking password", str(e))
    finally:
        return is_correct
