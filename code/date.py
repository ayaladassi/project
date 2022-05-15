import pandas as pd
import json

def put(name,role,guid):
  data=pd.read_csv('../data.csv')
  a=data['name'].size
  data.loc[a,'name']=name
  data.loc[a,'role']=role
  data.loc[a,'guid']=guid
  data.loc[a,'id']=a+1
  data.to_csv('../data.csv',index=False)

data = pd.read_csv('../data.csv')
print(data)
temp = data
a= '337b45ba-d444-11ec-92c5-4437e6d98dc5'
b=temp[temp['guid']==a]
print(b)
ee=b.to_json()
# temp.query('guid == a', inplace=True)
print(json.dumps(ee))





