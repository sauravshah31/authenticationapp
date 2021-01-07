import requests
import threading
import time
import os

from authorizerapp import init_app

class TestConfig:
    SECRET_KEY = "test123"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///test.db"

class Test:
    app = init_app(TestConfig)
    def __init__(self):
        self.t = threading.Thread(target=self.start_app)
        self.t.start()
        self.wait()
        self.test_register_route()
        self.test_login_route()
        self.test_verify_route()
        self.test_logout_route()
        self.t.join()
    

    def start_app(self):
        Test.app.run(port=7010)


    def test_register_route(self):
        # Test for only POST requets allowed
        response = requests.get("http://localhost:7010/api/register")
        assert(response.status_code == 405)
        response = requests.put("http://localhost:7010/api/register")
        assert(response.status_code == 405)
        response = requests.delete("http://localhost:7010/api/register")
        assert(response.status_code == 405)
        response = requests.post("http://localhost:7010/api/register")
        assert(response.status_code != 405)

        # Test for missing parameters
        headers = {'content-type' : 'application/json'}
        data = {}
        response = requests.post("http://localhost:7010/api/register",headers=headers,json=data)
        assert(response.status_code != 200)
        data["user_name"]="test"
        response = requests.post("http://localhost:7010/api/register",headers=headers,json=data)
        assert(response.status_code != 200)
        data["email"]="test@test.com"
        response = requests.post("http://localhost:7010/api/register",headers=headers,json=data)
        assert(response.status_code != 200)
        data["password"]="test"
        response = requests.post("http://localhost:7010/api/register",headers=headers,json=data)
        assert(response.status_code == 200)

        #Test for primarykey
        data["user_name"] = "test1"
        data["email"] = "test@test.com"
        response = requests.post("http://localhost:7010/api/register",headers=headers,json=data)
        assert(response.status_code != 200)
        data["user_name"] = "test"
        data["email"] = "test1@test.com"
        response = requests.post("http://localhost:7010/api/register",headers=headers,json=data)
        assert(response.status_code != 200)

        print('------------/api/register test passed------------')
        print()
        print()

    def test_login_route(self):
        # Test for only POST requets allowed
        response = requests.get("http://localhost:7010/api/login")
        assert(response.status_code == 405)
        response = requests.put("http://localhost:7010/api/login")
        assert(response.status_code == 405)
        response = requests.delete("http://localhost:7010/api/login")
        assert(response.status_code == 405)
        response = requests.post("http://localhost:7010/api/login")
        assert(response.status_code != 405)

        # Test for missing parameters
        headers = {'content-type' : 'application/json'}
        data = {}
        response = requests.post("http://localhost:7010/api/login",headers=headers,json=data)
        assert(response.status_code != 200)
        data["name"]="test"
        response = requests.post("http://localhost:7010/api/login",headers=headers,json=data)
        assert(response.status_code != 200)
        data["password"]="test"
        response = requests.post("http://localhost:7010/api/login",headers=headers,json=data)
        assert(response.status_code == 200)

        data["email"]="test@test.com"
        response = requests.post("http://localhost:7010/api/login",headers=headers,json=data)
        assert(response.status_code == 200)

        try:
            self.token = response.json()['token']
        except:
            assert(False)
        print('------------/api/login test passed------------')
        print()
        print()


    def test_verify_route(self):
        # Test for only GET requets allowed
        response = requests.put("http://localhost:7010/api/verify")
        assert(response.status_code == 405)
        response = requests.delete("http://localhost:7010/api/verify")
        assert(response.status_code == 405)
        response = requests.post("http://localhost:7010/api/verify")
        assert(response.status_code == 405)
        response = requests.get("http://localhost:7010/api/verify")
        assert(response.status_code != 405)

        #Test for missing token
        headers = {
            'content-type' : 'application/json'
        }
        response = requests.get('http://localhost:7010/api/verify',headers=headers)
        assert(response.status_code!=200)

        #Test for wrong token
        headers['x-access-token']='wrong.token.test'
        response = requests.get('http://localhost:7010/api/verify',headers=headers)
        assert(response.status_code!=200)

        #Test for right token
        headers['x-access-token']=self.token
        response = requests.get('http://localhost:7010/api/verify',headers=headers)
        assert(response.status_code==200)

        print('------------/api/verify test passed------------')
        print()
        print()

    def test_logout_route(self):
        # Test for only GET requets allowed
        response = requests.put("http://localhost:7010/api/logout")
        assert(response.status_code == 405)
        response = requests.delete("http://localhost:7010/api/logout")
        assert(response.status_code == 405)
        response = requests.post("http://localhost:7010/api/logout")
        assert(response.status_code == 405)
        response = requests.get("http://localhost:7010/api/logout")
        assert(response.status_code != 405)

        # Test for wrong token
        headers = {
            'content-type' : 'application/json'
        }
        headers['x-access-token']='wrong.token.test'
        response = requests.get('http://localhost:7010/api/logout',headers=headers)
        assert(response.status_code!=200 and response.status_code!=405)
    
        #Test for correct token
        headers['x-access-token']=self.token
        response = requests.get('http://localhost:7010/api/logout',headers=headers)
        assert(response.status_code==200)
        response = requests.get('http://localhost:7010/api/verify',headers=headers)
        assert(response.status_code!=200)
        print('------------/api/logout test passed------------')
        print()
        print()

    def wait(self):
        check = True
        while check:
            time.sleep(2)
            try:
                print(requests.get('http://localhost:7010/'))
                check = False
            except Exception as e:
                pass
    

t = Test()
print('----------Done---------')