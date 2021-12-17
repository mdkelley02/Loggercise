from flask_restx import Resource
from . import api

# create user endpoint
@api.route('/users')
class UserPost(Resource):
    def post(self):
        pass
