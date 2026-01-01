#%%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv',sep=';')

df.info()
#%%

filter_pts_bigger_50 = df['QtdePontos'] >= 50
print(len(filter_pts_bigger_50))

df[filter_pts_bigger_50]

#%%

filter_pts_between_50x100 = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100)

#The line below would do the same filter
# filter_pts_between_50x100 = (df['QtdePontos'] >= 50) * (df['QtdePontos'] < 100)
## replace '&' by '*'

df[filter_pts_between_50x100]

#%%

filter_pts_1_or_bigger_100 = (df['QtdePontos'] == 1) | (df['QtdePontos'] > 100)
#The line below would do the same filter
#filter_pts_1_or_bigger_100 = (df['QtdePontos'] == 1) + (df['QtdePontos'] > 100)
## replace '|' by '+'

df[filter_pts_1_or_bigger_100]