import requests
import json
from _datetime import datetime


def ping_server(url, json_data):
    try:
        response = requests.post(url, json=json_data)
    except requests.exceptions.ConnectionError:
        return 'Server unavailable'
    if response.status_code != 200:
        return 'Bad request'
    else:
        return json.loads(response.content.decode('utf-8'))

if __name__ == '__main__':
    app_setting_data = json.load(open("app_settings.json", "r"))
    host = app_setting_data['host']
    port = app_setting_data['port']
    url = f' http://{host}:{port}/'
    json_data_dict = {"jsonrpc": "2.0", "method": "ping", "params": {"time": str(datetime.now())}}
    json_data = json.dumps(json_data_dict)
    print(ping_server(url, json_data_dict))