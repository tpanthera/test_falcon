# create using json file

# store tyre data in json
# store tyre data in json
# retrieve from json with matching the id
# call it from rest api

'''
test json - {
  "Two": {
    "Size": "small , large",
    "Tube": "Tubeless , abc company tube",
    "Radius(meters)": "1,2,3",
    "thickness(cm)": "5,8,10"
  },
  "Four": {
    "Size": "small , large",
    "Tube": "Tubeless , abc company tube",
    "Radius(meters)": "1,2,3",
    "thickness(cm)": "5,8,10"
  },
  "Six": {
    "Size": "small , large",
    "Tube": "Tubeless , abc company tube",
    "Radius(meters)": "1,2,3",
    "thickness(cm)": "5,8,10"
  }
}

'''


import json,falcon

# create tyre details :
tyre_content_json = '{ }'
tyre_content_python = json.loads(tyre_content_json)

class tyre_class:
    def on_get(self,req,resp):
        if req.path == '/two_wheeler':
        #display content of two wheeler from pythonied json object
                try:
                    resp.body = json.dumps(tyre_content_python['Two'])
                except KeyError:
                    pass
        elif req.path == '/four_wheeler':
                try:
                    resp.body = json.dumps(tyre_content_python['Four'])
                except KeyError:
                    pass
        elif req.path == '/six_wheeler':
                try:                            
                    resp.body = json.dumps(tyre_content_python['Six'])
                except KeyError:
                    pass
        else:
             resp.body('Please enter valid wheeler type')    
            
api = falcon.API()
#dynamic routing
api_add_route('/{wheeler_type}', tyre_class())


'''
algo :
initiate the falcon api 

call class for any api
class :
    def On_get:
        if path is '/two_wheels'
            send_response_for two wheeler 
        if path is '/four_wheels'
            send_response_for four wheeler if path is '/two_wheels'
        if path is '/six_wheels'
            send_response_for six wheeler if path is '/two_wheels'         

dynamic api , store value in variable , call class
'''
