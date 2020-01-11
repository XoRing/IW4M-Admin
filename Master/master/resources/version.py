from flask_restful import Resource
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