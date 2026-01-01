#%%
#IMPORTS
import pandas as pd


#%%
#CONSTANTS
DATA_FOLDER_PATH = '../data/'

#%%
df = pd.read_csv(DATA_FOLDER_PATH +'transacao_produto.csv', sep=';')
df.info()
df.head()

#%%
# transactions with product id 5 and 11 (pandas see IdProduto as string  )
# filter = (df['IdProduto'] == '5') | (df['IdProduto'] == '11')

filter = df['IdProduto'].isin(["5","11"])

df[filter]

#%%

clients = pd.read_csv(DATA_FOLDER_PATH + 'clientes.csv', sep=';')

clients.info(memory_usage='deep')

#%%

filter = clients['DtCriacao'].isnull()

clients[filter]

#%%

neg_filter = ~clients['DtCriacao'].isnull()
print(filter)
print(neg_filter)
# clients[neg_filter]