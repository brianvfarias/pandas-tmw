#%%
import pandas as pd
transactions = pd.read_csv('../../data/transacoes.csv', sep=';')
transactions_products = pd.read_csv('../../data/transacao_produto.csv', sep=';')
#%%
# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
# 06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
# 06.03 - Qual usuário teve maior quantidade de pontos debitados?
#%%
# 06.04 - Quem teve mais transações de Streak?
print('joining the 2 dfs',
'did not worry much about how, since both dfs have almost the same amount of rows')
df = transactions_products.merge(
  transactions,
  on='IdTransacao'
)
print(df)

print("filtering the transactions that have the product 'Streak', which has id 12")
filter = df['IdProduto'] == '12'
streak_transactions = df[filter]
print(streak_transactions)

print("counting the number of transactions per customer")
transactions_by_customer = streak_transactions.groupby(by=['IdCliente'], as_index=False).agg({
  'IdTransacao': 'count'
})
print(transactions_by_customer)
transactions_by_customer.columns = ['Customer', 'CountOfTransactions']
print('updating the name of the columns')
print(transactions_by_customer)

print('sorting the customer based on the amount of transactions (descending)')
transactions_by_customer = transactions_by_customer.sort_values(by=['CountOfTransactions'], ascending=False)
print(transactions_by_customer)
print('showing the top customer')
transactions_by_customer.head(1)


# 06.05 - Qual a média de transações / dia?
# 06.06 - Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?
