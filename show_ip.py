from flask import Flask, jsonify, make_response
import requests
import json

app = Flask(__name__)
endpoint_url = 'http://icanhazip.com'
ipv4_endpoint_url = 'http://ipv4.icanhazip.com'

@app.route('/', methods=['GET'])
def proxy():
    try:
        response = requests.get(endpoint_url)
        print(response.content)
        return make_response(response.content, response.status_code)
    except requests.exceptions.RequestException as e:
        return make_response(str(e), 500)
    
@app.route('/ipv4', methods=['GET'])
def ipv4():
    try:
        response = requests.get(ipv4_endpoint_url)
        print(response.content)
        return make_response(response.content, response.status_code)
    except requests.exceptions.RequestException as e:
        return make_response(str(e), 500)

if __name__ == '__main__':
    app.run(port=8000, debug=True)