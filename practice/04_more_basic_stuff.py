#%%
import pandas as pd

df_transactions = pd.read_csv('../data/transacoes.csv', sep=';')

df_transactions.info()

#%%

df_transactions[['IdCliente', 'QtdePontos']].sample(5)

