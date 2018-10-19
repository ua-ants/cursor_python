import json

import flask
from flask import Flask
from flask import request


app = Flask(__name__)


HOST = '127.0.0.1'
PORT = 4000
DEBUG = False

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def check_member(name: str) -> bool:
    return name in MEMBERS.keys()


@app.route('/user', methods=['POST'])
@app.route('/user/<name>', methods=['GET', 'PATCH', 'DELETE'])
def profile(name: str):
    result = {}

    if flask.request.method == 'POST':
        params = json.loads(request.data.decode('utf-8'))
        MEMBERS[params.get('name')] = params
        result = {"status": "OK", "message": f"Add new user {params}"}

    if flask.request.method == 'GET':
        member = MEMBERS.get(name)
        if member is None:
            result = {"status": "Fail", "error": f"Could not find member with name {name}"}
        else:
            result = {"status": "OK", "message": f"We found your user {member}"}

    if flask.request.method == 'PATCH':
        member = MEMBERS.get(name)
        if member is None:
            result = {"status": "Fail", "message": "I don't know about such user. Sorry"}
        else:
            params = json.loads(request.data.decode('utf-8'))
            MEMBERS[name].update(params)
            result = {"status": "Ok", "message": f"This is your new member {MEMBERS.get(name)}"}

    if flask.request.method == 'DELETE':
        if not check_member(name):
            result = {"status": "Fail", "message": "I don't know about such user. Sorry"}
        else:
            del MEMBERS[name]
            result = {"status": "Ok", "message": f"We delete your member bro"}
    return json.dumps(result)

# Add route that will dump current states of members to json file
@app.route('/dump_users/<file_name>', methods=['GET'])
def dump_members(file_name: str):
    if flask.request.method =='GET':
        json.dump(MEMBERS, open(file_name, "w"))
        result = {"status": "OK", "message": f"File {file_name} created and saved"}
    else:
        result = {"status": "Fail", "error": "Unsupported method for the endpoint"}
    return json.dumps(result)

@app.route('/', methods=['GET'])
def default_route():
    return json.dump('OK')

if __name__ == '__main__':
    # Use data from json file to setup app.run method
    try:
        app_setting_data = json.load(open("app_settings.json", "r"))
    except FileNotFoundError:
        print('configuration file not found')
    else:
        app_setting_data = {'host': HOST, 'port': PORT, 'debug_mode': DEBUG}
    app.run(port=app_setting_data['port'],
            host=app_setting_data['host'],
            debug=app_setting_data['debug_mode'])
