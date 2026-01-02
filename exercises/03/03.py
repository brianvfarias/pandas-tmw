#%%
import pandas as pd

#%%
# 04.01 - Quantos clientes tem vínculo com a Twitch?
# First version
## filtering and showing the counts
df_clients = pd.read_csv('../../data/clientes.csv', sep=';')

# filter = df_clients['flTwitch'] == 1
# df_clients[filter].count()

amount_clients_twitch = df_clients['flTwitch'].value_counts()[1]

print('The amount of clients with twitch is', amount_clients_twitch)

# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?

filter = df_clients['qtdePontos'] > 1000

amount_clients_over_1000pts = len(df_clients[filter])

print('The amount of clients with over a thousand points is:', amount_clients_over_1000pts)

#%%
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?
df_transactions = pd.read_csv('../../data/transacoes.csv', sep=';')
filter = (df_transactions['DtCriacao'] >= '2025-02-01') & (df_transactions['DtCriacao'] < '2025-02-02')
amount_transactions_1st_feb = len(df_transactions[filter])

print("The amount of transactions in '2025-02-01' is:", amount_transactions_1st_feb)
