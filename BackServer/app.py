from flask import Flask, request, jsonify
from flask_jsonpify import jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

def init():
    #appelle a l'initialisation de la db
    print("appel main db")

@app.route('/test', methods=['POST'])
def add_tag():
    #ouverture connection db
    content = request.json
    id_annotation = content['id']
    #traitement requete base de données et renvoie en json les informations


    #fermeture connection db
    return jsonify({"Server":"Added : "+id_annotation})

init()

if __name__ == '__main__':
    app.run()
