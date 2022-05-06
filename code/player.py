from flask import Flask, request, jsonify, json
from flask_cors import CORS
import uuid
app = Flask(__name__)
CORS(app)



@app.route('/createGame', methods=['GET'])
def create_game():
    playerName = request.args.get('playerName')
    #hostname = request.headers.get('Host')
    guid = uuid.uuid1()
    #להחזיר לינק של המשחק כולל כתובת השרת + סלש + game + guid של המשחק
    return "http://127.0.0.1:8080/game/a9e86162-d472-11e8-b36c-ccaf789d94a0"