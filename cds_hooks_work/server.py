from flask import Flask, json
from flask_cors import CORS
import os
from cds_hooks_work.app import App

def serve(app: App, **kwargs):
    flaskApp = Flask(__name__)
    cors = CORS(app)
    debug = os.environ.get('DEBUG', False)

    @flaskApp.route('/cds-services')
    def discovery():
        return json.jsonify(app.discovery()), 200

    @app.route('/cds-services/{id}', methods=['POST'])
    def service(id):
        return "ok", 200