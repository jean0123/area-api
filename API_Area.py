from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)

class Area(Resource):
    '''
    Class to return the response of the api
    '''
    def get(self):
        return jsonify({"message": "Noting to do here"})
    def post(self):
        data = request.get_json()
        if data is None:
            return jsonify({"message": "No data provided"})
        else:
            height = data['height'] if 'height' in data else None
        if height is None:
            return jsonify({"message": "No height provided"})
        else:
            height = height.replace("[", "").replace("]", "")
            height = list(map(int, height.split(',')))
            if validate(height = height):
                return jsonify({"Max Area": maxArea(height = height)})
            else:
                return jsonify({"message": "Invalid input"})

def maxArea(height: list[int]) -> int:
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        max_area = max(max_area, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

def validate(height: list[int]) -> bool:
    if len(height) < 2:
        return False
    elif len(height) > 105:
        return False
    else:
        for i in height:
            if i < 1 or i > 105:
                return False
    return True

api.add_resource(Area, '/', methods=['POST', 'GET'])

if __name__ == '__main__':
    app.run()
