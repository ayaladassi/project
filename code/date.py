import pandas as pd
import json

def put(name,role,guid):
  data=pd.read_csv('../data.csv')
  a=data['name'].size
  data.loc[a,'name']=name
  data.loc[a,'role']=role
  data.loc[a,'guid']=guid
  data.loc[a,'id']=str(a+1)
  data.to_csv('../data.csv',index=False)

data = pd.read_csv('../data.csv')
print(data)
temp = data
a= '337b45ba-d444-11ec-92c5-4437e6d98dc5'
b=temp[temp['guid']==a]
print(b)
ee=b.to_json(orient="index")
# temp.query('guid == a', inplace=True)
print(json.loads(ee))
print(json.dumps(ee))
print(type(b[b["id"]=="4"]))
print(json.dumps([
        {"guid": f"{a}",
         "name": f"aaa",
         "role": f"aaaa",
         "id": "1"
         },
        {"guid": f"{a}",
         "name": f"bbbbbbbbbb",
         "role": f"bbbbbbbbbb",
         "id": "1"
         }
    ]))





