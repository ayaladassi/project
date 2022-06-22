import gensim
import random
import numpy as np
import inflect

model = gensim.models.KeyedVectors.load_word2vec_format(
    r'C:\Users\1\Documents\project\project\GoogleNews-vectors-negative300.bin.gz', binary=True, limit=200000
)

import os
import json
from queue import Queue
from enum import Enum
# class Role(Enum):
#     multi_spy = 0
#     spy=1
# class Color(Enum):
#     red = 0
#     blue =1
# def Color(self, color):
#         if color== "blue":
#             self.color = Color.blue
#         else:
#             self.color=Color.red
# def Role(self,role):
#         if role=="multi-spy":
#             self.role=Role.multi_spy
#         else:
#             self.role=Role.spy


class Game():
    arr=[0,0,0,0]
    def __init__(self):
        self.idPlayer=1
        self.queue = []
        self.groupRed=Group("red",9)
        self.groupBlue=Group("blue",8)
        self.bourd=bourd()
        self.platerNow=0
        self.grupNow="red"
        self.Humans=0
        self.wordClueNow=wordClue("","")
        self.groupBlue.words = self.bourd.blue
        self.groupBlue.bad_words = self.bourd.red + self.bourd.neutral + self.bourd.assassin
        self.groupRed.words = self.bourd.red
        self.groupRed.bad_words = self.bourd.blue + self.bourd.neutral + self.bourd.assassin
    def addPlayer(self,role,name,color,isHuman):
        if isHuman == True:
            self.Humans = self.Humans + 1
        if role=="multi-spy":
            if color=="red":
                if (self.groupRed.players and self.groupRed.players[0].role == "multi-spy") or len(self.groupRed.players)>1:
                        return False
            else:
                if (self.groupBlue.players and self.groupBlue.players[0].role == "multi-spy")or len(self.groupBlue.players)>1:
                        return False
        else:
            if color == "red":
                if self.groupRed.players and self.groupRed.players[0].role == "spy"or len(self.groupRed.players)>1:
                    return False
            else:
                if self.groupBlue.players and self.groupBlue.players[0].role == "spy"or len(self.groupBlue.players)>1:
                    return False

        player=Player(self.idPlayer,role,name,color,isHuman)
        self.queue.append(player)
        if player.color=="blue":
            self.groupBlue.players.append(player)
        else:
            self.groupRed.players.append(player)
        if color=="red" :
            if role == "multi-spy":
                self.arr[0] = 1
            elif role=="spy":
                self.arr[1]=1
        if color=="blue" :
            if role == "multi-spy":
                self.arr[2] = 1
            elif role=="spy":
                self.arr[3]=1
        self.idPlayer+=1
        playerJson=self.toJSONp(player)
        return playerJson

        # return player.id,player.role
    def getBoard(self):
        return self.bourd
    def getqueue(self):
        return self.queue
    def toJSON(self):
        return json.dumps(self.queue, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    def toJSONp(self,player):
        return json.dumps(player, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    def getarr(self):
        return self.arr
    def orderly_queue(self):
        global temparr
        temparr = []
        for i in range(len(self.queue)):
            temparr.append(self.queue[i])
        for i in range(len(self.queue)):
            if self.queue[i].role == "multi-spy":
                if self.queue[i].color == "red":
                    temparr[0] = self.queue[i]
                elif self.queue[i].color == "blue":
                   temparr[2] = self.queue[i]
            elif self.queue[i].role == "spy":
                if self.queue[i].color == "red":
                    temparr[1] = self.queue[i]
                elif self.queue[i].color == "blue":
                    temparr[3] = self.queue[i]
        for i in range(len(self.queue)):
            self.queue[i]=temparr[i]
    def Next_pleyer(self):
        self.platerNow += 1
        if self.platerNow>3:
            self.platerNow=0

    def isNexthuman(self):
        now=self.platerNow
        now+=1
        if now>3:
            now=0
        if self.queue[now].gethuman()==True:
            return True
        return False


    def Pressed_word(self,word,player):
        a=0
        for i in self.getBoard().getListBoard():
            if i.getWord()==word:
                print("aaaaaaaa")
                print(i.status)
                i.changeStatuss()
                print(i.status)


        if word in self.bourd.getred():
            self.bourd.getred().remove(word)
            self.groupRed.Score()
            print("rrrrrrrr")

        if word in self.bourd.getblue():
            self.bourd.getblue().remove(word)
            self.groupBlue.Score()
            print("bbbbbbbbbb")

        if word in self.bourd.getneutral():
            self.bourd.getneutral().remove(word)
            print("nnnnnnnnn")
        if word in self.bourd.getassassin():
            print("aassssssssss")
            for i in self.groupBlue.players:
               if player["id"] == i.getid():
                   self.groupRed.Score0()

            for i in self.groupRed.players:
                if player["id"] == i.getid():
                       self.groupBlue.Score0()

    def toJSONG(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)








class Group():
    words = []
    bad_words = []
    score=0
    def __init__(self,color,score):
        self.color=color
        self.score=score
        self.players=[]
    # def scorenew(self):
    #     if self.color=="red":
    #         self.score=9
    #     elif self.color=="blue":
    #         self.score=8
    def getScore(self):
        return self.score
    def getPlayer(self):
        return self.players
    def Score(self):
        self.score=self.score-1
    def Score0(self):
        self.score=0


    def guess(self,clue, words, n):
        poss = {}
        for w in words:
            poss[w] = model.similarity(clue, w)
        poss_lst = sorted(poss, key=poss.__getitem__, reverse=True)
        top_n = poss_lst[:n]
        return [w for w in top_n if poss[w] > 0.2]

    def clean_clue(self,word1, word2):
        engine = inflect.engine()
        word1 = word1.lower()
        word2 = word2.lower()
        return not (word1 in word2 or word2 in word1 or "_" in word2 or word2 == engine.plural(word1) or len(
            word2) <= 2)

    def give_clue(self,words, bad_words):
        # Correlates all possible pairs of words and store them in a dict of (word1,word2):similarity
        similarities = {}
        if len(words) >= 2:
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    similarities[(words[i], words[j])] = model.similarity(words[i], words[j])

        # Correlate all possible triplets of words and store them in a dict of (word1,word2,word3):similarity
        triple_similarities = {}
        if len(words) >= 3:
            seen = set()
            for w in words:
                for key in similarities.keys():
                    z = key + (w,)
                    if w not in key and tuple(sorted(z)) not in seen:
                        triple_similarities[z] = model.n_similarity([w], list(key))
                        seen.add(tuple(sorted(z)))

        # Loop until we find the optimal pair of words to give a clue for.
        while True:
            # If there is only 1 word left to guess or we run out of pairwise similarities,
            # set max_correlated_n to only word left
            if len(words) == 1 or not similarities:
                max_correlated_n = (words[0],)

            # If length is 2, set max_correlated_n to the max_correlated_pair
            elif len(words) >= 2:
                max_correlated_pair = max(similarities, key=similarities.get)
                max_correlated_n = max_correlated_pair

            # If length is 3, set max_correlated_n to:
            # max_correlated_triple if the triple similarity * 0.9 >= pair similarity
            # max_correlated_pair otherwise
            # 0.9 can be tuned based on experimental data
            if len(words) >= 3:
                max_correlated_triple = max(triple_similarities, key=triple_similarities.get)
                if triple_similarities[max_correlated_triple] * 0.9 >= similarities[max_correlated_pair]:
                    max_correlated_n = max_correlated_triple
                else:
                    max_correlated_n = max_correlated_pair

            print("Giving clue for:", max_correlated_n)
            c_words = list(max_correlated_n)

            # Find most similar words to words in max_correlated_n
            clues = model.most_similar(positive=c_words, topn=10, restrict_vocab=10000)

            # Clean the found similar words
            clues_dict = dict(clues)
            cleaned_clues = [c[0] for c in clues if all([self.clean_clue(w, c[0]) for w in c_words])]

            # Iterate until cleaned_clues is empty or we find an optimal clue
            while cleaned_clues:
                # Find best current clue
                possible_clue = max(cleaned_clues, key=lambda x: clues_dict[x])

                # If game is nearing end, skip filtering of clues
                if len(words) == len(max_correlated_n):
                    return possible_clue, tuple(max_correlated_n)

                # Find most similar word to best current clue from bad_words
                enemy_match = model.most_similar_to_given(possible_clue, bad_words)

                # Calculate similarity between the two
                enemy_sim = model.similarity(enemy_match, possible_clue)

                # If enemy's word is greater in similarity than any of the words in max_correlated_pair,
                # remove the best current clue from cleaned_clues and continue iterating.
                # If not, return the current clue, as it is optimal.
                optimal = True
                for n in max_correlated_n:
                    if enemy_sim >= model.similarity(n, possible_clue):
                        print("Foreign word " + enemy_match + " was too similar. Removing clue: " + possible_clue)
                        cleaned_clues.remove(possible_clue)
                        optimal = False
                        break

                if optimal:
                    return possible_clue, tuple(max_correlated_n)

            # All the enemy's clues were atleast more similar than one of the words in max_correlated_pair,
            # so pop max_correlated_n from corresponding similarities dict and continue iterating.
            print("Too many enemy correlations. Removing ", max_correlated_n)
            if len(max_correlated_n) == 2:
                similarities.pop(max_correlated_n)
            elif len(max_correlated_n) == 3:
                triple_similarities.pop(max_correlated_n)

class Player():

    def __init__(self,idPlayer,role,name,color,isHuman):
        self.id=idPlayer
        self.role=role
        self.color=color
        self.name=name
        self.human=isHuman
    def getColor(self):
        return self.color
    def getid(self):
        return self.id
    def gethuman(self):
        return self.human








class bourd():
    listBoard=[]
    red = []
    blue = []
    neutral = []
    assassin = []
    dict1 = {}
    def __init__(self):
        with open(r"..\words.txt", encoding="utf8") as f:
          self.words = f.readlines()
        self.words = [w.strip() for w in self.words]
        self.board, self.red, self.blue, self.neutral,self.assassin=self.generate_board(self.words)
        self.listToDict()
    def generate_board(self,word_list):
            used = set()
            red = []
            blue = []
            neutral = []
            assassin = []

            # Generate 9 random words for r+ed team.
            while len(red) < 9:
                index = random.choice(range(len(word_list)))
                word = word_list[index]
                if index not in used:
                    red.append(word)
                    used.add(index)

            # Generate 8 random words for blue team.
            while len(blue) < 8:
                index = random.choice(range(len(word_list)))
                word = word_list[index]
                if index not in used:
                    blue.append(word)
                    used.add(index)

            # Generate 7 random neutral words.
            while len(neutral) < 7:
                index = random.choice(range(len(word_list)))
                word = word_list[index]
                if index not in used:
                    neutral.append(word)
                    used.add(index)

            # Generate assassin word.
            while not assassin:
                index = random.choice(range(len(word_list)))
                word = word_list[index]
                if index not in used:
                    assassin.append(word)
                    used.add(index)
            board = red + blue + neutral + assassin
            random.shuffle(board)
            # board = np.reshape(board, (5, 5))

            return board, red, blue, neutral, assassin
    def listToDict(self):
       for i in self.red:
            self.dict1[f'{i}']="red"
       for i in self.blue:
           self.dict1[f'{i}'] = "blue"
       for i in self.neutral:
           self.dict1[f'{i}'] = "yellow"
       for i in self.assassin:
           self.dict1[f'{i}'] = "black"
       # print(self.dict1)
       l = list(self.dict1.items())
       random.shuffle(l)
       self.dict1 = dict(l)
       self.listBoard=[]
       for key,value in self.dict1.items():
           word1=word(key,value)
           self.listBoard.append(word1)
    def getListBoard(self):
        return self.listBoard
    def getblue(self):
        return self.blue
    def getred(self):
        return self.red
    def getneutral(self):
        return self.neutral
    def getassassin(self):
        return self.assassin
    def changeStatus(self,word):
        for i in self.listBoard:
            if word == i:
                i.changeStatuss()

    def toJSON(self):
        return json.dumps(self.listBoard, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)



class wordClue():
    def __init__(self,word,number):
        self.word=word
        self.number=number
    def toJSONw(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class word():
    def __init__(self,word,color):
        self.word=word
        self.color=color
        self.status=False
    def getWord(self):
        return self.word
    def changeStatuss(self):
        self.status=True
class gameStatus():
    def __init__(self):
        self.playerNow=Player(0,"","","",True)
        self.word_Clue=wordClue("",0)
        self.messages=[]
        self.listBoard=[]
        self.score_red=9
        self.score_blue=8
        self.lenm=len(self.messages)
    def setword_Clue(self,word):
        self.word_Clue=word

    def setplayerNow(self, player):
        self.playerNow = player

    def setmessages(self, mas):
        self.messages.append(mas)
    def setmessageslen(self):
        self.lenm=len(self.messages)

    def setlistBoard(self, listBoard):
        self.listBoard = listBoard
    def toJSONGS(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)




# b=Game()
# f=b.addPlayer("multi-spy","das3","blue",False)
# t=b.addPlayer("multi-spy","dasooo1","red",True)
# yy=b.addPlayer("spy","dassiooo2","red",True)
# a=b.addPlayer("spy","dassi4","blue",True)
# h=b.addPlayer("spy","dassiyyyyy4","blue",True)
# b.queue[0].name
# print(b.Humans)
# print(f)
# print(a)
# print(t)
# print(yy)
# print(h)
# for x in range(len(b.queue)):
#     print(b.queue[x].name)
# print(" ")
# b.orderly_queue()
# for x in range(len(b.queue)):
#     print (b.queue[x].name)
# print(b.groupBlue.give_clue(b.groupBlue.words,b.groupBlue.bad_words))
# print(b.bourd.dict1)
# g=b.bourd.listToDict()
# # print(b.arr)
# print(b.bourd.getblue()+b.bourd.getred())
# a=input("enter")
# l=['king', 'ketchup', 'whale', 'agent', 'fall', 'europe', 'log', 'truck', 'opera', 'dwarf', 'alien', 'lawyer', 'air', 'green', 'staff', 'stadium', 'server']
#
# print(b.groupRed.guess(a,l,2))










