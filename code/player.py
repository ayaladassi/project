from flask import Flask, request, jsonify, json
from flask_cors import CORS
import uuid
import pandas as pd
import json


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
    playercolor = request_data['color']
    guid = uuid.uuid1()
    data = pd.read_csv('../data.csv')
    a = data['name'].size
    data.loc[a, 'name'] = playername
    data.loc[a, 'role'] = playerrole
    data.loc[a, 'guid'] = guid
    data.loc[a, 'id'] = a+1
    data.loc[a,'color']=playercolor
    data.to_csv('../data.csv', index=False)
    print(playername,playerrole,guid,a+1,playercolor)
    b=data[data['guid'] == guid]
    print(b)
    # result = b.to_json(orient="index")
    # parsed = json.loads(result)
    # b=data[data['guid'] == guid]
    

    # return parsed

    return json.dumps([
        {"guid": f"{guid}",
         "name": f"{playername}",
         "role": f"{playerrole}",
         "id": a + 1,
         "color":f"{playercolor}"
         },
        {"guid": f"{guid}",
         "name": f"{playername}",
         "role": f"{playerrole}",
         "id": a + 1,
         "color":f"{playercolor}"
         }
    ])
@app.route('/JoinGame', methods=['POST'])
def Join_game():
    request_data = request.get_json()
    playername = request_data['name']
    playerrole = request_data['role']
    playerguid = request_data['guid']
    playercolor = request_data['color']


    data = pd.read_csv('../data.csv')
    a = data['name'].size
    data.loc[a, 'name'] = playername
    data.loc[a, 'role'] = playerrole
    data.loc[a, 'guid'] = playerguid
    data.loc[a, 'id'] = a + 1
    data.loc[a,'color']=playercolor
    data.to_csv('../data.csv', index=False)
    print(playername, playerrole,playerguid, a + 1,playercolor)
    return json.dumps([
        {"guid": f"{playerguid}",
         "name": f"{playername}",
         "role": f"{playerrole}",
         "id": a + 1,
         "color":f"{playercolor}"
         },
        {"guid": f"{playerguid}",
         "name": f"{playername}",
         "role": f"{playerrole}",
         "id": a + 1,
         "color":f"{playercolor}"
         }
    ])

@app.route('/getPlayer', methods=['GET'])
def get_Player():
    data = pd.read_csv('../data.csv')
    print(data)
    request_data = request.get_json()
    guid=request_data['guid']
    # data.query('guid' == guid, inplace=True)
    print(data)
    return {
        data[data['guid'] == guid]
    }
@app.route('/startGame',methods=['GET'])
def start_game():
    request_data = request.get_json()
    guid=request_data['guid']
    return{
        guid
    }

@app.route('/checkStartGame',methods=['GET'])
def check_start_game():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)