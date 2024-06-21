from flask import Flask, request, jsonify
from flask_restful import Api, Resource

from utilities import checkPostedData

app = Flask(__name__)
api = Api(app)


# Add Function  
class Add(Resource):
    def post(self):
        # if we are here, then the resource Add was requested using the POST method
        
        # Step 1: Get posted data
        postedData = request.get_json()
        
        # Step 1b: verify validity of posted data
        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                'Status Code': status_code
            }
            return jsonify(retJson)
        
        # If we are here, then status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        
        # Step 2: add data
        ret = x+y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        
        # Step 3: Return a response
        return jsonify(retMap)

        
# Subtract function
class Subtract(Resource):
    def post(self):
    # if we are here, then the resource Sustract was requested using the POST method
    
        # Step 1: Get posted data
        postedData = request.get_json()
        
        # Step 1b: verify validity of posted data
        status_code = checkPostedData(postedData, "subtract")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                'Status Code': status_code
            }
            return jsonify(retJson)
        
        # If we are here, then status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        
        # Step 2: subtract data
        ret = x-y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        
        # Step 3: Return a response
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
    # if we are here, then the resource Multiply was requested using the POST method
    
        # Step 1: Get posted data
        postedData = request.get_json()
        
        # Step 1b: verify validity of posted data
        status_code = checkPostedData(postedData, "multiply")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                'Status Code': status_code
            }
            return jsonify(retJson)
        
        # If we are here, then status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        
        # Step 2: multiply data
        ret = x*y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        
        # Step 3: Return a response
        return jsonify(retMap)





class Divide(Resource):
    def post(self):
    # if we are here, then the resource Divide was requested using the POST method
    
        # Step 1: Get posted data
        postedData = request.get_json()
        
        # Step 1b: verify validity of posted data
        status_code = checkPostedData(postedData, "division")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                'Status Code': status_code
            }
            return jsonify(retJson)
        
        # If we are here, then status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        
        # Step 2: divide data. make sure it is a float
        ret = (x*1.0)/y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        
        # Step 3: Return a response
        return jsonify(retMap)





api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
    
