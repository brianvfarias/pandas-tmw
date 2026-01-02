#%% 
import pandas as pd
import numpy as np
clients = pd.read_csv('../data/clientes.csv',sep=';')

# column 'pts_plus_100' does not exists
clients.head()

clients['pts_plus_100'] = clients['qtdePontos'] + 100

# column 'pts_plus_100' exists with the 'qtdePontos' + 100 for each element
clients.head()

#%%
# sorting a column/serie of the original dataframe
clients['qtdePontos'].sort_values()

# sorting the whole dataframe by a given column
clients.sort_values(by='qtdePontos',ascending=False)

# sorting based on many columns in a dataframe
# descending sort based on the qtdePontos
# ascending sort based on the DtCriacao

clients.sort_values(by=['qtdePontos', 'DtCriacao'], ascending=[False, False])
