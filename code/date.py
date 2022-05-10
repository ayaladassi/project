import pandas as pd

def put(name,role,guid):
  data=pd.read_csv('C:/Users/1/Documents/פרויקט בעזרה/project/data.csv')
  a=data['name'].size
  data.loc[a,'name']=name
  data.loc[a,'role']=role
  data.loc[a,'guid']=guid
  data.loc[a,'id']=a+1

  print(data)
  data.to_csv('C:/Users/1/Documents/פרויקט בעזרה/project/data.csv',index=False)
  temp = data
  temp.query('guid == 3', inplace=True)
  print(temp)
put("aa","eee",3)
put("aa","eee",1)
put("aa","eee",3)
put("aa","eee",55)
data = pd.read_csv('C:/Users/1/Documents/פרויקט בעזרה/project/data.csv')
print(data)
temp = data
temp.query('guid == 3', inplace=True)
print(temp)




