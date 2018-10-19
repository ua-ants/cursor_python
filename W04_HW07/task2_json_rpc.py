from flask import Flask
from flask import request

import json

app = Flask(__name__)

HOST = '127.0.0.1'
PORT = 4000
DEBUG = False

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}

# create function that will return JSON-RPC success valid response
# create function that will return JSON-RPC response
def json_rpc_valid_response(result):
    response_data = {"jsonrpc": "2.0"}
    response_data["result"] = result
    return json.dumps(response_data)

def json_rpc_response(rpc_method, **params):
    if rpc_method not in METHODS.keys():
        return json.dumps({"error": {"code": -32601, "message": "Method not found"}})
    return METHODS[rpc_method](**params)

def add_member(name, age, gender):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    return json_rpc_valid_response(f"We add your member {MEMBERS[name]}")

# Create implementation for getMember method
def get_member(name):
    return json_rpc_valid_response(MEMBERS[name])

def ping(time):
    return json_rpc_valid_response(f"pong {time}")


METHODS = {
    "getMember": get_member,
    "addMember": add_member,
    "ping": ping
}


@app.route('/', methods=['POST'])
def handle():
    print(request.data.decode('utf-8'))
    data = json.loads(request.data.decode('utf-8'))
    rpc_method = data.get('method')
    return json_rpc_response(rpc_method, **data.get("params"))


if __name__ == '__main__':
    try:
        app_setting_data = json.load(open("app_settings.json", "r"))
    except FileNotFoundError:
        print('configuration file not found')
    else:
        app_setting_data = {'host': HOST, 'port': PORT, 'debug_mode': DEBUG}
    app.run(port=app_setting_data['port'],
            host=app_setting_data['host'],
            debug=app_setting_data['debug_mode'])
