from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
import json

class Version(Resource):
    def get(self, api_version = 0):
        if api_version == 0:
            config = json.load(open('./master/config/master.old.json'))
        else:
            config = json.load(open('./master/config/master.json'))
        return { 
            'current-version-stable' : config['current-version-stable'],
            'current-version-prerelease' : config['current-version-prerelease']
         }, 200

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('current-version-stable', help='Stable version must be provided', required = True)
        parser.add_argument('current-version-prerelease', help='Prerelease version must be provided', required = True)
        args = parser.parse_args()

        with open('./master/config/master.json', 'w') as out_json:
            json.dump(args, out_json, indent=4)

        return {'message': 'updated'}