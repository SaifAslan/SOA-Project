from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask("UserLoginAPI")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("username", required=True)
parser.add_argument("userpassword", required=True)

users = {
    "Adham": {
        "username": "Adham",
        "useremail": "test@gmail.com",
        "userpassword": "test123",
        "usertype": "1",
        "usermobilenumber": "1234567",
    },
    "Joe": {
        "username": "Joe",
        "useremail": "joe@gmail.com",
        "userpassword": "joe123",
        "usertype": "2",
        "usermobilenumber": "75499436",
    },
}


class UserLogin(Resource):
    def get(self, user_name):
        try:
            if user_name.lower() == "all":
                return users
            return users[user_name], 200
        except:
            return 404


api.add_resource(UserLogin, "/userlogin/<user_name>")


if __name__ == "__main__":
    app.run()
