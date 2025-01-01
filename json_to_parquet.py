import pandas as pd
import os

base_path = os.getcwd()
json_path = os.path.join(base_path,"itemLookUp.json")
parquet_path = os.path.join(base_path,"itemLookUp.parquet")

df = pd.read_json(json_path)
df.to_parquet(parquet_path, engine="pyarrow")

df_parquet = pd.read_parquet(parquet_path)
df_parquet[1][1][0]
df_parquet.shape