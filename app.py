from flask import Flask, request, render_template, make_response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app=app, origins=['http://192.168.0.100:8023'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['GET','POST'])
def location():
    if request.method == 'GET':
        loc = json.load(open('currentLocation.json', 'r'))
        return loc
    elif request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        try:
            data = json.loads(request.data)
            json.dump(data, open('currentLocation.json', 'w'))
            return ('status', 200)
        except Exception as e:
            return str(e)
