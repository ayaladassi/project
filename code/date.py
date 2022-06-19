# import pandas as pd
# import json
import random

# def put(name,role,guid):
#   data=pd.read_csv('../data.csv')
#   a=data['name'].size
#   data.loc[a,'name']=name
#   data.loc[a,'role']=role
#   data.loc[a,'guid']=guid
#   data.loc[a,'id']=str(a+1)
#   data.to_csv('../data.csv',index=False)
#
# data = pd.read_csv('../data.csv')
# print(data)
# temp = data
# a= '337b45ba-d444-11ec-92c5-4437e6d98dc5'
# b=temp[temp['guid']==a]
# print(b)
# ee=b.to_json(orient="index")
# # temp.query('guid == a', inplace=True)
# print(json.loads(ee))
# print(json.dumps(ee))
# print(type(b[b["id"]=="4"]))
# print(json.dumps([
#         {"guid": f"{a}",
#          "name": f"aaa",
#          "role": f"aaaa",
#          "id": "1"
#          },
#         {"guid": f"{a}",
#          "name": f"bbbbbbbbbb",
#          "role": f"bbbbbbbbbb",
#          "id": "1"
#          }
#     ]))
class bourd():
    red = []
    blue = []
    neutral = []
    assassin = []
    dict1 = {}
    listBoard=[]
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
            # board = np.reshape(board, (5, 5))

            return board, red, blue, neutral, assassin
    def listToDict(self):
       for i in self.red:
            self.dict1[f'{i}']="red"
       for i in self.blue:
           self.dict1[f'{i}'] = "blue"
       for i in self.neutral:
           self.dict1[f'{i}'] = "neutral"
       for i in self.assassin:
           self.dict1[f'{i}'] = "assassin"
       print(self.dict1)
       for key,value in self.dict1.items():
           word1=word(key,value)
           self.listBoard.append(word1)
    def Pressed_word(self,b,word,player):
        for i in b.listBoard:
            if i.word==word:
                i.changeStatus()

        if word in b.red:
            b.red.remove(word)
            if len(b.red):
               print("red")
               # return "red"

            else:
                 return "The red team wins"

        if word in b.blue:
            b.blue.remove(word)
            if len(b.blue):
               print("red")

               # return "blue"
            else:
                return "The blue team wins"

        if word in b.neutral:
            b.neutral.remove(word)
            print("neutral")

            # return "neutral"

class word():
    def __init__(self,word,color):
        self.word=word
        self.color=color
        self.status=False
    def changeStatus(self):
        self.status=True


b=bourd();
b.listToDict()
l = list(b.dict1.items())
random.shuffle(l)
d = dict(l)
print(d)
listBoard=[]
for key, value in d.items():
    word1 = word(key, value)
    listBoard.append(word1)
for i in listBoard:
    print(i.word,i.color,i.status)
print(b.Pressed_word(b,"club","a"))

