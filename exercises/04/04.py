#%%
import pandas as pd

# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
# 05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
# 05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?

# 05.05 - Selecione a primeira transação diária de cada cliente.
#%%

transactions = pd.read_csv('../../data/transacoes.csv', sep=';')
def removeTime(datetxt: str):
  return datetxt[0:11]

transactions = transactions.sort_values(by=['DtCriacao'])
transactions['Data'] = transactions['DtCriacao'].apply(removeTime)
first_transaction_day_x_client = transactions.drop_duplicates(subset=['IdCliente', 'Data'])
first_transaction_day_x_client

#%%
# challenge solved using a sample client that had many transactions, just to simplify the checking of the outputs provided
# sample_client = '24782f0b-4683-4f35-976a-ea21d6714ba6'

# filter = transactions['IdCliente'] == sample_client
# #%%
# sample_transactions = (transactions[filter][['DtCriacao', 'QtdePontos']])
# sample_transactions
# #%%
# sample_transactions = sample_transactions.sort_values(by=['DtCriacao'])
# sample_transactions
# #%%



# sample_transactions['DtCriacao'] = sample_transactions['DtCriacao'].apply(removeTime)

# sample_transactions
# #%%
# sample_transactions = sample_transactions.drop_duplicates(keep='first',subset='DtCriacao')
# sample_transactions