# %%
import pandas as pd

df = pd.read_csv("./data/clientes.csv")

df.to_parquet("./clientes.parquet", index=False)

df2 = pd.read_parquet("./clientes.parquet")

print(df2)
