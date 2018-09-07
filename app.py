# simple rest api based on falcon

import json,falcon

class obRequestClass:
    def on_get(self,req,resp):
        content = {
            'name' : 'Manish' ,
            'place' : 'Bengaluru'
        }
        resp.body = json.dumps(content)

api = falcon.API()
api.add_route('/test',objRequestClass())


'''
Run in command line
gunicorn app:api


'''
