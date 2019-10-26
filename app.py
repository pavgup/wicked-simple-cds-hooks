from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)


@app.route("/cds-services")
def cdsServices():
    with open('cds-services.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)
    #return "Hello World!"


@app.route("/cds-services/medication-predict", methods = ['GET', 'POST'])
def medicationPredict():
    #print(request.headers)
    #content = request.json
    #print(content)
    with open('static-predict.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)


if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=443, debug=True, ssl_context='adhoc')
    app.run(host='0.0.0.0', port=80, debug=True)
