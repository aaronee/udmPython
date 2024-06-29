from flask import Flask, jsonify, request
from flask_restful import Api, Resource #remember to add "resource" here

app = Flask(__name__)
api = Api() #"Api" is a constructor to construct a RESTful api object

def checkPostedData(data, funcName):
    if 'x' not in data or 'y' not in data:
        return 301
    else:
        if(funcName == "divide"):
            if data['y'] == 0:
                return 302
        else:
            return 200

'''
"resource" is understand as a function that server is offering; For example: add, subtract, divine, multiply...
'''
class Add(Resource):
    def post(self): #if I am here then the resource Add was requested using POST
        postData = request.get_json()
        errCode = checkPostedData(postData, "add")
        if 200 != errCode:
            errJson = {
                "error code":errCode,
                "message":"invalid params"
            }
            return errJson, errCode
        x = int(postData['x'])
        y = int(postData['y'])
        ret = x + y
        retMap = {
            'Sum':ret,
            'Status Code': 200
        }
        return jsonify(retMap)
    def get(self):
        return "There is nothing for GET"   
class Subtract(Resource):
    def post(self):
        postData = request.get_json()
        errCode = checkPostedData(postData, "subtract")
        if 200 != errCode:
            errJson = {
                "error code":errCode,
                "message":"invalid params"
            }
            return errJson, errCode
        x = int(postData['x'])
        y = int(postData['y'])
        ret = x - y
        retMap = {
            'subtract':ret,
            'Status Code': 200
        }
        return jsonify(retMap)
    def get(self):
        return "There is nothing for GET"

class Multiply(Resource):
    def post(self):
        postData = request.get_json()
        errCode = checkPostedData(postData, "multiply")
        if 200 != errCode:
            errJson = {
                "error code":errCode,
                "message":"invalid params"
            }
            return errJson, errCode
        x = int(postData['x'])
        y = int(postData['y'])
        ret = x * y
        retMap = {
            'multiply':ret,
            'Status Code': 200
        }
        return jsonify(retMap)
    def get(self):
        return "There is nothing for GET"
class Divide(Resource):
    def post(self):
        postData = request.get_json()
        errCode = checkPostedData(postData, "divide")
        if 200 != errCode:
            errJson = {
                "error code":errCode,
                "message":"invalid params"
            }
            return errJson, errCode
        x = int(postData['x'])
        y = int(postData['y'])
        ret = x / y
        retMap = {
            'divide':ret,
            'Status Code': 200
        }
        return jsonify(retMap)
    def get(self):
        return "There is nothing for GET"

api.add_resource(Add, "/add") #This is the standard route method under Flask RESTful; more at https://flask-restful.readthedocs.io/en/latest/
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

api.init_app(app)

if __name__ == "__main__":
    '''
    Default will be localHost
    To docker container to listen to the request, we add host='0.0.0.0' (or >>flask run --host='0.0.0.0') so the server in docker will listen to all TCP address
    Read more at https://stackoverflow.com/questions/20778771/what-is-the-difference-between-0-0-0-0-127-0-0-1-and-localhost
    '''
    app.run(debug=True)
    

