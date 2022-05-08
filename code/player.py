from flask import Flask, request, jsonify, json
from flask_cors import CORS
import uuid
import pandas as pd

app = Flask(__name__)
CORS(app)

data = pd.read_excel(r"C:\Users\212318026\PycharmProjects\project\data.xlsx")
data.loc[len(data.index)] = ['Amy', 89, 93]


@app.route('/')
def hello():
    return 'hello'

@app.route('/createGame', methods=['GET'])
def create_game():
    playername = str(request.args.get('playerName'))
    playerrole = str(request.args.get('playerRole'))
    #hostname = request.headers.get('Host')
    guid = uuid.uuid1()
    data.loc[len(data.index)] = [playername, playerrole,guid]

    #הכנסה לרשימת שחקנים
    return {"link": f"http://192.168.49.42:8000/game/{guid}",
            "name": f"{playername}",
            "role": f"{playerrole}"
    }
@app.route('/JoinGame', methods=['GET'])
def Join_game():
    playername = str(request.args.get('playerName'))
    playerrole = str(request.args.get('playerRole'))

#הצטרפות לרשימת שחקנים
    return
@app.route('getPlayer', methods=['GET'])
def get_Player():

    return {
        #רשימת שחקנים
    }
@app.route('/startGame',methods=['GET'])
def start_game():
    return
@app.route('/checkStartGame',methods=['GET'])
def check_start_game():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)