from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(resource):
    def get(self):
        return {'about':'Hello World'}

    def post(self):
        rec_json = request.get_json()
        return {'You\'ve sent':rec_json}, 201

class Multiply(Resource):
    def get(self, num):
        return {'result':num*10}

api.add_resource(HelloWorld, '/')
api.add_resource(Multiply, 'multiply/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)

