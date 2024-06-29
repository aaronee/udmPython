from flask import Flask, jsonify, request

'''
"Flask" is a constructor to construct a FLASK app object
'''
app = Flask(__name__)

'''
This is the default route method of Flask, not the RESTful API route method of flask_restful
'''
@app.route("/hello", methods=["POST"]) #by default, the route will support GET only
def sayHello2Hi():
    inJson = request.get_json() # "request" module to get the input json from client
    if "hi" not in inJson:
        return "Error no valid data", 302 # 302 here is the return error code
    else:
        retJson = {
            'name': "Khoa",
            'hello': True
        }
        return jsonify(retJson), 200

if __name__ == "__main__":
    app.run(debug=True)

'''
From terminal config the app object and run server:
>> export FLASK_APP=app1_introFlask.py
>> flask run
'''