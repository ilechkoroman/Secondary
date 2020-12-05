from flask import Blueprint
from flask_restplus import Api

from app.api.namespaces import secondary as secondary_ns
from app.api.secondary import routes as secondary


API_VERSION_V1 = 1

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_v1_bp)


secondary_ns.add_resource(secondary.POST, '/post')
secondary_ns.add_resource(secondary.Delete, '/delete')
secondary_ns.add_resource(secondary.GET, '/get')


api_v1.add_namespace(secondary_ns, '/secondary')

