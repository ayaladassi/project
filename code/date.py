import pandas as pd

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
a= '63eb598c-d16b-11ec-aa9c-0045e21826b0'
print(temp[temp['guid']==a])
# temp.query('guid == a', inplace=True)




