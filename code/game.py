import random
import numpy as np
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
    def __init__(self):
        self.idGame=1
        self.queue = []
        self.groupRed=Group("red")
        self.groupBlue=Group("blue")
        self.bourd=board()
        self.platerNow=0
        self.Humans=0
    def addPlayer(self,role,name,color,isHuman):
        if isHuman == True:
            self.Humans = self.Humans + 1
        if role=="multi_spy":
            if color=="red":
                if (self.groupRed.players and self.groupRed.players[0].role == "multi_spy") or len(self.groupRed.players)>1:
                        return False
            else:
                if (self.groupBlue.players and self.groupBlue.players[0].role == "multi_spy")or len(self.groupBlue.players)>1:
                        return False
        else:
            if color == "red":
                if self.groupRed.players and self.groupRed.players[0].role == "spy"or len(self.groupRed.players)>1:
                    return False
            else:
                if self.groupBlue.players and self.groupBlue.players[0].role == "spy"or len(self.groupBlue.players)>1:
                    return False

        player=Player(role,name,color,isHuman)
        self.queue.append(player)
        if player.color=="blue":
            self.groupBlue.players.append(player)
        else:
            self.groupRed.players.append(player)
        return True
    def orderly_queue(self):
        for multi in self.queue:
            if multi.role=="mu":
                pass


class Group():
    def __init__(self,color):
        self.color=color
        self.score=0
        self.players=[]

class Player():
    def __init__(self,role,name,color,isHuman):
        self.role=role
        self.color=color
        self.name=name
        self.human=isHuman



class board():
    red = []
    blue = []
    neutral = []
    assassin = []
    def __init__(self):
        with open(r"..\words.txt", encoding="utf8") as f:
          self.words = f.readlines()
        self.words = [w.strip() for w in self.words]
        self.board, self.red, self.blue, self.neutral,self.assassin=self.generate_board(self.words)
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
            board = np.reshape(board, (5, 5))
            return board, red, blue, neutral, assassin
class wordClue():
    def __init__(self,word,group):
        self.word=word
        self.group=group
b=Game()

f=b.addPlayer("multi_spy","das","blue",False)
g=b.addPlayer("multi_spy","das","blue",True)
a=b.addPlayer("spy","dassi","blue",True)
c=b.addPlayer("spy","das","blue",True)

print(b.Humans)
print(f)
print(g)
print(a)
print(c)






