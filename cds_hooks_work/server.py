from flask import Flask, json, request
from flask_cors import CORS

def serve(app, **kwargs):
    flaskApp = Flask(__name__)
    CORS(flaskApp)

    @flaskApp.route('/cds-services')
    def discovery():
        return json.jsonify(app.discovery()), 200

    @flaskApp.route('/cds-services/<id>', methods=['POST'])
    def service(id):
        requestData = request.json
        try:
            response = app.handle_hook(id, requestData)
            body = response.to_dict()
            return json.jsonify(body), response.httpStatusCode
        except:
            return "client error", 400

    flaskApp.run(**kwargs)