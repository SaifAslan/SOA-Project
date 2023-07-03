from database_connection import connect_to_databse, app, logging


@app.route("/getuser/<user_name>", methods=["GET"])
def get_user(user_name):
    connection = connect_to_databse()
    try:
        # run query
        cursor = connection.cursor()
        sql = f"""SELECT * FROM users WHERE username = '{user_name}'"""
        cursor.execute(sql)
        row = cursor.fetchall()
        logging.debug("Query executed")
        return row
    except Exception as e:
        logging.exception("Exception while executing query", str(e))
        return "Error occured while fetching user details"
    finally:
        cursor.close()
        connection.close()
