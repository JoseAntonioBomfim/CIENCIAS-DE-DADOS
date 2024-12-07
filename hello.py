import pandas as pd

dados = {'Nome': ['Ana', 'Bruno', 'Carla'],'Idade':[21, 20, 22]}

df = pd.DataFrame(data = dados)

df.to_csv('dados.csv')

df = pd. read_csv('dados.csv', index_col = 0, header = 0)
print(df)