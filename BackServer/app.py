from flask import Flask, request, jsonify
from flask_jsonpify import jsonify
from flask_restful import Resource, Api

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test', methods=['POST'])
def add_tag():
    content = request.json
    id_annotation = content['id']
    return jsonify({"Server":"Added : "+id_annotation})



if __name__ == '__main__':
    app.run()
