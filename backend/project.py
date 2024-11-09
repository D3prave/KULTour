import pandas as pd
import numpy as np

df = pd.read_csv('good_data.csv', encoding='utf-16', low_memory=False)
print(df.head())
# print(f"Number of columns before dropping: {df.shape[1]}")
# df.dropna(axis=1, how='all', inplace=True)
# print(f"Number of columns after dropping: {df.shape[1]}")
# df = df.loc[:, df.count() >= 250]
# print(f"Number of columns after dropping columns with less than 50 rows: {df.shape[1]}")
# column_names = df.columns.tolist()
# print("Column names:", column_names)
# with open('temp.csv', 'w') as f:
#   for column in column_names:
#     f.write(f"{column}\n")
    
columns_to_keep = ['pageTitle (actionDetails 0)', 'visitorType', 'visitCount', 'continent', 'country']

df = df.loc[:, columns_to_keep]

# Print the updated DataFrame to confirm
print("Updated DataFrame with only selected columns:")
print(df)
df.to_csv('test123.csv', index=False)