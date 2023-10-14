from flask import Flask, request, render_template, make_response
import json

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run('0.0.0.0', port=8023)