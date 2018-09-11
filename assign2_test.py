import falcon 
import pytest

class Tyre:
	def __init__():
		self.width =

	#setter 
	#getter 

	def on_post(self, req, resp):
		if(req.path == two_wheel):
			two_wheel_call = two_wheel()

		if(req.path == four_wheel):
			four_wheel_call = four_wheel()

		if(req.path == six_wheel):
			six_wheel_call = six_wheel()

class two_wheel(Tyre):
	# implemenation for retrievinh json for 2_wheeler
class four_wheel(Tyre):

class six_wheel(Tyre):

application = falcon.API()
application.add_route(/{wheel_type}, Tyre())

# python test framework 

# create main class , call that , which inturn will call api class and get the assert thing 

#You must create an `app` fixture to expose the Falcon application you want to test:

@pytest.fixture
def app():
return application

# test_ to discover the method to be tested 

## Fixtures ### client
'''
def test_post(client):
resp = client.post('/route', {'myparam': 'myvalue'})
assert resp.status == falcon.HTTP_OK
assert resp.json['myparam'] == 'myvalue'
'''

