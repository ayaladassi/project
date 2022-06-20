from flask import Flask, request, jsonify, json
from flask_cors import CORS
import uuid
import pandas as pd
import json
from game import *


app = Flask(__name__)
CORS(app)
global game1
game1 = Game()

@app.route('/')
def hello():
    return 'hello'

@app.route('/createGame', methods=['POST'])
def create_game():

    request_data = request.get_json()
    playername= request_data['name']
    playerrole = request_data['role']
    playercolor = request_data['color']

    id,role=game1.addPlayer(playerrole,playername,playercolor,True)
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
    print(game1.queue[0].name)
    print(id)
    if id==False:
        return f"{False}"
    # return f"{id,role}"
    return json.dumps([
        {
         "role": f"{role}",
         "id": f"{id}"
         }
    ])



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



    # return json.dumps([
    #     {   # {"guid": f"{guid}",
    #      "name": f"{playername}",
    #      "role": f"{playerrole}",
    #      "id":  1,
    #      "color":f"{playercolor}"
    #      }
    #     # ,
    #     # {"guid": f"{guid}",
    #     #  "name": f"{playername}",
    #     #  "role": f"{playerrole}",
    #     #  "id": a + 1,
    #     #  "color":f"{playercolor}"
    #     #  }
    # ])
@app.route('/JoinGame', methods=['POST'])
def Join_game():
    request_data = request.get_json()
    playername = request_data['name']
    playerrole = request_data['role']
    # playerguid = request_data['guid']
    playercolor = request_data['color']
    id,role = game1.addPlayer(playerrole, playername, playercolor, True)
    # print(game1.queue[1].name)
    for i in game1.getqueue():
        print(i.name,i.role,i.color)



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
    if id==False:
        return f"{False}"
    # return f"{id}"
    return json.dumps([
        {
         "role": f"{role}",
         "id": f"{id}"
         }
    ])



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


    return game1.toJSON()
@app.route('/startGame',methods=['GET'])
def start_game():
    if game1.getarr()[0]==0:
        game1.addPlayer("multi-spy","dani","red",False)
    if game1.getarr()[1]==0:
        game1.addPlayer("spy","shemesh","red",False)
    if game1.getarr()[2]==0:
        game1.addPlayer("multi-spy","chani","blue",False)
    if game1.getarr()[3]==0:
        game1.addPlayer("spy","sari","blue",False)
    game1.orderly_queue()
    for i in game1.getqueue():
        print(i.name,i.role,i.color)
    bool=True
    return f"{bool}"
@app.route('/getBoard',methods=['GET'])
def get_Board():
    return game1.getBoard().toJSON()
@app.route('/clickButton',methods=['POST'])
def click_Button():
    request_data = request.get_json()
    word = request_data['word']
    print(word)

    # player=request_data['word']
    return word

@app.route('/nextPleyer',methods=['GET'])
def Next_pleyer():
    game1.Next_pleyer()
    if game1.queue[game1.platerNow].human==False:
        if game1.platerNow==0:
            aword=game1.groupRed.give_clue(game1.bourd.red,game1.bourd.blue+game1.bourd.neutral+game1.bourd.assassin)
        if game1.platerNow==2:
            aword=game1.groupBlue.give_clue(game1.bourd.blue,game1.bourd.red+game1.bourd.neutral+game1.bourd.assassin)
        game1.Next_pleyer()
        return aword
    bool=True
    return f"{bool}"
@app.route('/giveClue',methods=['GET'])
def Give_Clue():
    request_data = request.get_json()
    word=wordClue(request_data['word'],request_data['color'])
    if game1.queue[game1.Next_pleyer()].human==False:
        if word.group=="red":6512230




@app.route('/checkStartGame',methods=['GET'])
def check_start_game():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)