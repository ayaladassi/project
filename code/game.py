import gensim
import random
import numpy as np
import inflect

model = gensim.models.KeyedVectors.load_word2vec_format(
    r'C:\Users\1\Documents\project\project\GoogleNews-vectors-negative300.bin.gz', binary=True, limit=200000
)
print()

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
        self.bourd=bourd()
        self.platerNow=0
        self.grupNow="red"
        self.Humans=0
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

        player=Player(role,name,color,isHuman)
        self.queue.append(player)
        if player.color=="blue":
            self.groupBlue.players.append(player)
            self.groupBlue.words=self.bourd.blue
            self.groupBlue.bad_words=self.bourd.red+self.bourd.neutral+self.bourd.assassin
        else:
            self.groupRed.players.append(player)
            self.groupRed.words = self.bourd.red
            self.groupRed.bad_words = self.bourd.blue + self.bourd.neutral + self.bourd.assassin
        return True
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
        if self.platerNow<3:
            self.platerNow+=1
        elif self.platerNow==3:
            self.platerNow=0

    def Pressed_word(self,word,player):
        if word in self.bourd.red:
            self.bourd.red.remove(word)
            if len(self.bourd.red):
               return "red"
            else:
                return "The red team wins"

        if word in self.bourd.blue:
            self.bourd.blue.remove(word)
            if len(self.bourd.blue):
               return "blue"
            else:
                return "The blue team wins"

        if word in self.bourd.neutral:
            self.bourd.neutral.remove(word)
            return "neutral"
        if word in self.bourd.assassin:
            if player in self.groupBlue.players:
                return "The blue team wins"
            elif player in self.groupRed.players:
                return "The red team wins"






class Group():
    words = []
    bad_words = []
    def __init__(self,color):
        self.color=color
        self.score=0
        self.players=[]


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
    def __init__(self,role,name,color,isHuman):
        self.role=role
        self.color=color
        self.name=name
        self.human=isHuman

class bourd():
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
f=b.addPlayer("multi-spy","das3","blue",False)
t=b.addPlayer("multi-spy","dasooo1","red",True)
yy=b.addPlayer("spy","dassiooo2","red",True)
a=b.addPlayer("spy","dassi4","blue",True)
h=b.addPlayer("spy","dassiyyyyy4","blue",True)
b.queue[0].name
print(b.Humans)
print(f)
print(a)
print(t)
print(yy)
print(h)
for x in range(len(b.queue)):
    print(b.queue[x].name)
print(" ")
b.orderly_queue()
for x in range(len(b.queue)):
    print (b.queue[x].name)
print(b.groupBlue.give_clue(b.bourd.red,b.bourd.blue+b.bourd.assassin+b.bourd.neutral))











