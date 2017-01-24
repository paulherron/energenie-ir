from flask import Flask, jsonify, Response
from flask_cors import CORS, cross_origin
import datetime
import json
import os
import sys
app = Flask(__name__)
CORS(app)

status_file_path = os.path.dirname(__file__) + '/status.json'

@app.route('/')
def status():
    return get_status()

@app.route('/down')
def down():
    os.system('irsend SEND_ONCE Lutron_MaestroIR DOWN --count=5')
    update_status('down')
    return get_status()

@app.route('/up')
def up():
    os.system('irsend SEND_ONCE Lutron_MaestroIR UP --count=5')
    update_status('up')
    return get_status()

@app.route('/on')
def on():
    os.system('irsend SEND_ONCE Lutron_MaestroIR ON')
    update_status('on')
    return get_status()

@app.route('/off')
def off():
    os.system('irsend SEND_ONCE Lutron_MaestroIR OFF')
    update_status('off')
    return get_status()

def update_status(status):
    with open(status_file_path, 'w') as status_file:
        json.dump({'lastCommand': status, 'lastCommandTime': datetime.datetime.now().isoformat()}, status_file)

def get_status():
    with open(status_file_path, 'r') as status_file:
        return Response(status_file.read(), mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
