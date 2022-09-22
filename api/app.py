from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.resources.driver_resource import DriverResource
from api.resources.results_resource import ResultsResource

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(DriverResource, '/driver')
api.add_resource(ResultsResource, '/results')

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000)