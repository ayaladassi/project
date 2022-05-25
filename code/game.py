import random
import numpy as np
import os
import json
class Game():
    def __init__(self,idGame,tor,link,bourd):
        self.tor=tor
        self.idGame=idGame
        self.link=link
        self.bourd=bourd
class Group():
    def __init__(self,color):
        self.color=color
        self.score=0

class Player():
    def __init__(self,type,name,color):
        self.type=type
        self.name=name
        self.group=Group(color)
class board():
    def __init__(self):
        with open("C:/Users/212318026/PycharmProjects/project/code/words.txt", encoding="utf8") as f:
            words = f.readlines()
        words = [w.strip() for w in words]
        self.board, self.red, self.blue, self.neutral,self.assassin=self.generate_board(words)
    def generate_board(word_list):
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
            print(red)
            return board, red, blue, neutral, assassin

with open(r"C:\Users\1\Documents\project\project\words.txt", encoding="utf8") as f:
    words = f.readlines()
words = [w.strip() for w in words]

def generate_board(word_list):
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
            # print(red)
            return board, red, blue, neutral, assassin
bboard,red,blue,neutral,assassin=generate_board(words)
print(bboard)
print( )
print(red)
print( )

print(blue)
print( )

print(neutral)
print( )

print(assassin)





