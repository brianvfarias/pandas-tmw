#%% 
import pandas as pd

#%%
# 03.01 - Quantas linhas há no arquivo clientes.csv ?
df_clients = pd.read_csv('../../data/clientes.csv', sep=';')
amount_of_rows, amount_of_columns = df_clients.shape
print('There are',amount_of_rows, 'rows and', amount_of_columns, 'columns in the df_clientes')

#%%
# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?

df_transactions = pd.read_csv('../../data/transacoes.csv', sep=';')
filter = df_transactions.dtypes == 'int64'
transactions_int_columns = df_transactions.dtypes[filter]
print('The amount of in columns in df_transactions is', len(list(transactions_int_columns)))



#%%
# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
df_products = pd.read_csv('../../data/produtos.csv', sep=';')
print(df_products.dtypes)

filter = df_products.dtypes == 'object'

products_object_columns = df_products.dtypes[filter]

print('The amount of object columns in produtos.csv is:', len(list(products_object_columns)))

#%%
# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
df_clients = pd.read_csv('../../data/clientes.csv', sep=';')


print(df_clients.head())

client_idx4 = df_clients.iloc[4]
print(client_idx4['idCliente'])


#%%
# 03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?

df_clients = pd.read_csv('../../data/clientes.csv', sep=';')

client_idx10 = df_clients.iloc[10]
print(client_idx10)
print(client_idx10['qtdePontos'])
print(client_idx10.loc['qtdePontos'])

