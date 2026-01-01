#%%
import pandas as pd

df_clients = pd.read_csv("../data/clientes.csv", sep=";")

print(df_clients)


# Show n first rows (n defaults to 5)
df_clients.head(n=10)


# # Show n last rows (n defaults to 5)
df_clients.tail(n=7)

# Show n random rows (n defaults to 5)
df_clients.sample(10)

# A tuple with (qty_rows, qty_columns)
df_clients.shape

# Shows the available columns in the DataFrame 
df_clients.columns
#%%
# Shows descriptive information about each and every data column
## memory_usage='deep' shows the exact amount of memory comsumed by the df
df_clients.info(memory_usage='deep')
# A less descriptive version of info(). Only shows data types of columns
df_clients.dtypes


