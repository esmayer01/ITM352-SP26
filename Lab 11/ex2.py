# Read in a CSV file and create a dataframe
# Print some useful info

import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/....csv"  # real CSV link, not Drive "view"
df = pd.read_csv(url)  # or pd.read_parquet(...), etc.

pd.set_option('display.max_columns', None)

df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['sales'] = df['quantity'] * df['unit_price']

pivot_table = df.pivot_table(
    values='sales',
    index='sales_region',
    columns='order_type',
    aggfunc=np.sum,
    margins=True,
    margins_name='Total Sales'
)
print(pivot_table)