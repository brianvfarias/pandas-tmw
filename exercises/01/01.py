# %%
import pandas as pd

#%%
# Leia o arquivo transacoes.csv com a formatação correta;
# Adicione uma coluna com valores 1;
# Salve o dataframe com nome: transacoes_1.csv
df_transactions = pd.read_csv('../../data/transacoes.csv', sep=';')
#%%

df_transactions.head()
df_transactions['valores1'] = 1
df_transactions.head()

df_transactions.to_parquet('./transacoes1.parquet', index=False)

df_transactions.to_csv('./transacoes1.csv', sep=';', index=False)

#%%
df_transactions1_parquet = pd.read_parquet('./transacoes1.parquet')


df_transactions1_parquet.head()
