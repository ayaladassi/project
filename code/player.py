from flask import Flask, request, jsonify, json
from flask_cors import CORS
import uuid
import pandas as pd
import json
from game import *
import time



app = Flask(__name__)
CORS(app)
global game1
game1 = Game()
global gameS
gameS=gameStatus()


@app.route('/')
def hello():
    return 'hello'

@app.route('/createGame', methods=['POST'])
def create_game():

    request_data = request.get_json()
    playername= request_data['name']
    playerrole = request_data['role']
    playercolor = request_data['color']

    player=game1.addPlayer(playerrole,playername,playercolor,True)


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
    print(player)
    if player==False:
        return f"{False}"
    # return f"{id,role}"
    # return json.dumps([
    #     {
    #      "role": f"{role}",
    #      "id": f"{id}"
    #      }
    # ])
    return player



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
    player=game1.addPlayer(playerrole,playername,playercolor,True)
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
    if player==False:
        return f"{False}"
    # return f"{id}"
    return player



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
    game1.starGame=True

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
    gameS.queue=game1.queue
    gameS.setmessages(game1.queue[game1.platerNow].name+" player now")
    gameS.setmessageslen()

    gameS.setplayerNow(game1.queue[game1.platerNow])
    gameS.setlistBoard(game1.bourd.getListBoard())
    boola=True
    return f"{boola}"

@app.route('/getBoard',methods=['GET'])
def get_Board():
    return game1.getBoard().toJSON()

@app.route('/clickButton',methods=['POST'])
def click_Button():

    request_data = request.get_json()
    word = request_data['word']
    player = request_data['player']
    if player["id"] == game1.queue[game1.platerNow].getid():
        game1.Pressed_word(word, player)
        gameS.setlistBoard(game1.bourd.getListBoard())
        gameS.setmessages(player["name"] + " play now")
        gameS.setmessageslen()

        gameS.setplayerNow(player)
        gameS.score_red=game1.groupRed.getScore()
        gameS.score_blue=game1.groupBlue.getScore()
        return f"{True}"
    else:
        return f"{False}"


@app.route('/nextPleyer',methods=['POST'])
def Next_pleyer():
    request_data = request.get_json()
    player = request_data['player']
    gameS.playerNow = game1.queue[game1.platerNow]

    gameS.setmessages("Now it's " + gameS.playerNow.name + "'s turn")

    print(player)
    if player["id"]==game1.queue[game1.platerNow].getid() or game1.queue[game1.platerNow].gethuman()==False:
        aa = []
        game1.Next_pleyer()
        gameS.playerNow = game1.queue[game1.platerNow]
        gameS.word_Clue = game1.wordClueNow
        gameS.setmessages("Now it's " + gameS.playerNow.name + "'s turn")
        gameS.setmessageslen()


        aword = ()
        if game1.queue[game1.platerNow].human == False:
            if game1.platerNow == 0:
                aword = game1.groupRed.give_clue(game1.bourd.getred(),
                                                 game1.bourd.getblue() + game1.bourd.getneutral() + game1.bourd.getassassin())
                game1.wordClueNow=wordClue(aword[0],len(aword[1]))
                gameS.setword_Clue(game1.wordClueNow)
                gameS.setmessages(gameS.playerNow.name+"give a clue: "+aword[0])
                gameS.setmessageslen()
                time.sleep(1)


                if game1.isNexthuman()==True:
                    game1.Next_pleyer()
                    gameS.playerNow = game1.queue[game1.platerNow]
                    gameS.setmessages("Now it's " + gameS.playerNow.name + "'s turn")
                    gameS.setmessageslen()

                    return f"nurmal"
                else:
                    return f"{True}"
                # game1.Next_pleyer()
                # return f"{aword[0]}"
                # return json.dumps(
                #     {
                #         "word": f"{aword[0]}",
                #         "len": f"{len(aword[1])}",
                #         "player": game1.toJSONp(game1.getqueue()[game1.platerNow])
                #
                #     }
                # )
            if game1.platerNow == 2:
                aword = game1.groupBlue.give_clue(game1.bourd.getblue(),
                                                  game1.bourd.getred() + game1.bourd.getneutral() + game1.bourd.getassassin())
                game1.wordClueNow=wordClue(aword[0],len(aword[1]))
                gameS.setword_Clue(game1.wordClueNow)
                gameS.setmessages(gameS.playerNow.name+"give a clue: "+aword[0])
                gameS.setmessageslen()
                time.sleep(1)


                if game1.isNexthuman()==True:
                    game1.Next_pleyer()
                    gameS.playerNow = game1.queue[game1.platerNow]
                    gameS.setmessages("Now it's " + gameS.playerNow.name + "'s turn")
                    gameS.setmessageslen()

                    return f"nurmal"
                else:
                    return f"{True}"

                # game1.Next_pleyer()
                # return json.dumps(
                #     {
                #         "word": f"{aword[0]}",
                #         "len": f"{len(aword[1])}",
                #         "player": game1.toJSONp(game1.getqueue()[game1.platerNow])
                #
                #     }
                # )
            if game1.platerNow == 1:
                list_gusses = game1.groupRed.guess(game1.wordClueNow.word,
                                                   game1.bourd.getblue() + game1.bourd.getred() + game1.bourd.getneutral() + game1.bourd.getassassin(),
                                                   game1.wordClueNow.number)
                print(list_gusses)
                gameS.setmessages("Now it's " + gameS.playerNow.name + " player")
                for i in list_gusses:
                    print(i)
                    game1.Pressed_word(i, player)

                gameS.score_red=game1.groupRed.getScore()
                gameS.score_blue=game1.groupBlue.getScore()

                gameS.setlistBoard(game1.bourd.getListBoard())
                time.sleep(2)

                if game1.isNexthuman()==True:
                    game1.Next_pleyer()
                    gameS.playerNow = game1.queue[game1.platerNow]
                    gameS.setmessages("Now it's " + gameS.playerNow.name + "'s turn")
                    gameS.setmessageslen()

                    return f"nurmal"
                else:
                    return f"{True}"
            if game1.platerNow == 3:
                list_gusses = game1.groupBlue.guess(game1.wordClueNow.word,
                                                    game1.bourd.getblue() + game1.bourd.getred() + game1.bourd.getneutral() + game1.bourd.getassassin(),
                                                    game1.wordClueNow.number)
                print(list_gusses)

                for i in list_gusses:
                    game1.Pressed_word(i, player)

                gameS.score_blue=game1.groupBlue.getScore()
                gameS.score_red=game1.groupRed.getScore()

                gameS.setlistBoard(game1.bourd.getListBoard())
                time.sleep(2)

                if game1.isNexthuman()==True:
                    game1.Next_pleyer()
                    gameS.playerNow = game1.queue[game1.platerNow]
                    gameS.setmessages("Now it's " + gameS.playerNow.name + "'s turn")
                    gameS.setmessageslen()
                    return f"nurmal"
                else:
                    return f"{True}"
        else:
           return f"nurmal"
    else:
        return f"{False}"


@app.route('/giveClue',methods=['POST'])
def Give_Clue():
    request_data = request.get_json()
    player=request_data['player']
    word_Clue=request_data['word']
    worda=word_Clue['word']
    num=int(word_Clue['num'])
    if player["id"]==game1.queue[game1.platerNow].getid():
        game1.wordClueNow = wordClue(worda, num)
        gameS.playerNow = game1.queue[game1.platerNow]
        gameS.word_Clue = game1.wordClueNow
        print(gameS.messages)
        gameS.setmessages("Now it's " + gameS.playerNow.name + "'s turn")

        if game1.isNexthuman() == True:
            print(gameS.playerNow.name)
            game1.Next_pleyer()
            gameS.playerNow = game1.queue[game1.platerNow]
            gameS.setmessages("Now it's " + gameS.playerNow.name + "'s turn")

            return f"nurmal"
        else:
            return f"{True}"

        # game1.Next_pleyer()
        # if game1.queue[game1.platerNow].human == False:
        #     if game1.queue[game1.platerNow].color == "red":
        #         list_gusses = game1.groupRed.guess(worda,
        #                                            game1.bourd.getblue() + game1.bourd.getred() + game1.bourd.getneutral() + game1.bourd.getassassin(),
        #                                            num)
        #         print(list_gusses)
        #         for i in list_gusses:
        #             print(i)
        #             red, blue = game1.Pressed_word(i, player)
        #             print(red, blue)
        #         return f"{True}"
        #     if game1.queue[game1.platerNow].color == "blue":
        #         list_gusses = game1.groupBlue.guess(worda,
        #                                             game1.bourd.getblue() + game1.bourd.getred() + game1.bourd.getneutral() + game1.bourd.getassassin(),
        #                                             num)
        #         print(list_gusses)
        #
        #         for i in list_gusses:
        #             red,blue=game1.Pressed_word(i, player)
        #             print(red, blue)
        #
        #         return f"{True}"


        # return game1.toJSONp(game1.getqueue()[game1.platerNow])
    else:
        return f"{False}"

@app.route('/getGame',methods=['GET'])
def get_game():
    return game1.toJSONG()

@app.route('/getPlayerNow',methods=['GET'])
def get_Player_Now():
    return game1.toJSONp(game1.getqueue()[game1.platerNow])
@app.route('/getClue',methods=['GET'])
def get_Clue():
    return game1.wordClueNow.toJSONw()
@app.route('/getGameStatus',methods=['GET'])
def get_game_Status():
    return gameS.toJSONGS()





@app.route('/checkStartGame',methods=['GET'])
def check_start_game():
    return f"{game1.starGame}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)




def Give_Clue____():
    request_data = request.get_json()
    player=request_data['player']
    word_Clue=request_data['word']
    worda=word_Clue['word']
    num=int(word_Clue['num'])
    if player["id"]==game1.queue[game1.platerNow].getid():
        game1.wordClueNow = wordClue(worda, num)
        game1.Next_pleyer()
        if game1.queue[game1.platerNow].human == False:
            if game1.queue[game1.platerNow].color == "red":
                list_gusses = game1.groupRed.guess(worda,
                                                   game1.bourd.getblue() + game1.bourd.getred() + game1.bourd.getneutral() + game1.bourd.getassassin(),
                                                   num)
                print(list_gusses)
                for i in list_gusses:
                    print(i)
                    game1.Pressed_word(i, player)

                return f"{True}"
            if game1.queue[game1.platerNow].color == "blue":
                list_gusses = game1.groupBlue.guess(worda,
                                                    game1.bourd.getblue() + game1.bourd.getred() + game1.bourd.getneutral() + game1.bourd.getassassin(),
                                                    num)
                print(list_gusses)

                for i in list_gusses:
                    red,blue=game1.Pressed_word(i, player)
                    print(red, blue)

                return f"{True}"

        else:
            return game1.toJSONp(game1.getqueue()[game1.platerNow])
    else:
        return f"{False}"