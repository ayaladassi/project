from flask import Flask, request, jsonify, json
from flask_cors import CORS
import uuid
import pandas as pd


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'hello'

@app.route('/createGame', methods=['POST'])
def create_game():
    request_data = request.get_json()
    playername= request_data['name']
    playerrole = request_data['role']
    guid = uuid.uuid1()
<<<<<<< Updated upstream
    data = pd.read_csv('C:/Users/212318026/PycharmProjects/project/data.csv')
    a = data['name'].size
    data.loc[a, 'name'] = playername
    data.loc[a, 'role'] = playerrole
    data.loc[a, 'guid'] = guid
    data.loc[a, 'id'] = a+1
    data.to_csv('C:/Users/212318026/PycharmProjects/project/data.csv', index=False)
    print(playername,playerrole,guid,a+1)

    return {"link": f"http://192.168.49.42:8000/game/{guid}",
            "name": f"{playername}",
            "role": f"{playerrole}",
            "id":a+1
    }
@app.route('/JoinGame', methods=['POST'])
def Join_game():
    request_data = request.get_json()
    playername = request_data['name']
    playerrole = request_data['role']
    guid = uuid.uuid1()
    data = pd.read_csv('C:/Users/212318026/PycharmProjects/project/data.csv')
    a = data['name'].size
    data.loc[a, 'name'] = playername
    data.loc[a, 'role'] = playerrole
    data.loc[a, 'guid'] = guid
    data.loc[a, 'id'] = a + 1
    data.to_csv('C:/Users/212318026/PycharmProjects/project/data.csv', index=False)
    print(playername, playerrole, guid, a + 1)

@app.route('/getPlayer', methods=['GET'])
def get_Player():
    data = pd.read_csv('C:/Users/1/Documents/פרויקט בעזרה/project/data.csv')
    print(data)
    data.query('guid == 3', inplace=True)
    print(data)
    return {
        data
    }
@app.route('/startGame',methods=['GET'])
def start_game():
    return
@app.route('/checkStartGame',methods=['GET'])
def check_start_game():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
=======
    #להחזיר לינק של המשחק כולל כתובת השרת + סלש + game + guid של המשחק
    return "http://127.0.0.1:8080/game/a9e86162-d472-11e8-b36c-ccaf789d94a0"
guid = uuid.uuid1()
print(guid)
>>>>>>> Stashed changes
