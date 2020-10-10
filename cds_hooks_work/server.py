from flask import Flask, json, request
from flask_cors import CORS
import os
from cds_hooks_work.app import App

def serve(app: App, **kwargs):
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
            return "ok", 200
        except:
            return "client error", 400

    flaskApp.run(**kwargs)