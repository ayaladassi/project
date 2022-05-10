import pandas as pd

def put(name,role,guid):
  data=pd.read_csv('C:/Users/212318026/PycharmProjects/project/data.csv')
  a=data['name'].size
  data.loc[a,'name']=name
  data.loc[a,'role']=role
  data.loc[a,'guid']=guid
  data.loc[a,'id']=a+1
  print(data)
  data.query('Senior_Management == True', inplace=True)
  data.to_csv('C:/Users/212318026/PycharmProjects/project/data.csv',index=False)
put("aa","eee",3)
