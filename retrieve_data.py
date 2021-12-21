from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "dedrich" : {
        "age" : 27,
        "gender" : "male",
    },
    "reinhard" : {
        "age" : 20,
        "gender" : "male",
    },
    "Giovany" : {
        "age" : 18,
        "gender" : "female",
    },
}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
