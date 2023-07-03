from database_connection import app
from user_authentication import authenticate_user
from user_credentials_registration import register_user_credentials

# instantiate the web methods
authenticate_user
register_user_credentials


if __name__ == "__main__":
    app.run()
