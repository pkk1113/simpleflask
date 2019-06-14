from flask_restful import Resource


class HomeAPI(Resource):
    URI = "/"

    def get(self):
        return "Hello Ngnix"

