from flask import Flask, request, jsonify, json
from flask_cors import CORS
import uuid
import pandas as pd
import json
from game import *


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
    global game
    game = Game()
    bool=game.addPlayer(playerrole,playername,playercolor,True)
    # guid = uuid.uuid1()
    # data = pd.read_csv('../data.csv', encoding='cp1252')
    #
    # a = data['name'].size
    # data.loc[a, 'name'] = playername
    # data.loc[a, 'role'] = playerrole
    # data.loc[a, 'guid'] = 3
    # data.loc[a, 'id'] = str(a+1)
    # data.loc[a,'color']=playercolor
    # data.to_csv('../data.csv', index=False)
    print(playername,playerrole,playercolor)
    print(game.queue[0].name)

    # b=data[data['guid'] == guid]
    # print(b)
    # result = b.to_json(orient="index")
    # parsed = json.loads(result)
    # b=data[data['guid'] == guid]
    # b=data[data['guid'] == 3]
    # print(b)
    # print(type(b))
    # json_list = b.to_json(orient='columns')
    # print(json_list)

    # return f"{bool}"


    return json.dumps([
        {   # {"guid": f"{guid}",
         "name": f"{playername}",
         "role": f"{playerrole}",
         "id": a + 1,
         "color":f"{playercolor}"
         }
        # ,
        # {"guid": f"{guid}",
        #  "name": f"{playername}",
        #  "role": f"{playerrole}",
        #  "id": a + 1,
        #  "color":f"{playercolor}"
        #  }
    ])
@app.route('/JoinGame', methods=['POST'])
def Join_game():
    request_data = request.get_json()
    playername = request_data['name']
    playerrole = request_data['role']
    # playerguid = request_data['guid']
    playercolor = request_data['color']
    bool = game.addPlayer(playerrole, playername, playercolor, True)
    print(game.queue[1].name)



    # data = pd.read_csv('../data.csv')
    # a = data['name'].size
    # data.loc[a, 'name'] = playername
    # data.loc[a, 'role'] = playerrole
    # data.loc[a, 'guid'] = playerguid
    # data.loc[a, 'id'] = a + 1
    # data.loc[a,'color']=playercolor
    # data.to_csv('../data.csv', index=False)
    # print(playername, playerrole,playerguid, a + 1,playercolor)
    # return json.dumps([
    #     {"guid": f"{playerguid}",
    #      "name": f"{playername}",
    #      "role": f"{playerrole}",
    #      "id": a + 1,
    #      "color":f"{playercolor}"
    #      },
    #     {"guid": f"{playerguid}",
    #      "name": f"{playername}",
    #      "role": f"{playerrole}",
    #      "id": a + 1,
    #      "color":f"{playercolor}"
    #      }
    # ])
    return f"{bool}"



@app.route('/getPlayer', methods=['GET'])
def get_Player():
    # data = pd.read_csv('../data.csv')
    # print(data)
    # request_data = request.get_json()
    # # guid=request_data['guid']
    # guid='9f8846e4-db4b-11ec-9fd2-4437e6d98dc5'
    # b = data[data['guid'] == guid]
    # print(b)
    # json_list = json.dumps(b.to_json(orient="records"))
    # print(data)
    # return {
    #     json_list
    # }
    return game.queue
@app.route('/startGame',methods=['GET'])
def start_game():
    # request_data = request.get_json()
    # guid=request_data['guid']
    game.orderly_queue()
    bool=True
    return f"{bool}"

@app.route('/checkStartGame',methods=['GET'])
def check_start_game():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)