from flask import Flask
from flask_restful import Api
from api.resources.driver_resource import DriverResource

app = Flask(__name__)
api = Api(app)

api.add_resource(DriverResource, '/driver')

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000)