#%%
import pandas as pd

transactions = pd.read_csv('../data/transacoes.csv', sep=';')

clients = pd.read_csv('../data/clientes.csv', sep=';')
transactions.info()

#%%

transactions.merge(right=clients, how='left', left_on=['IdCliente'], right_on=['idCliente'])

