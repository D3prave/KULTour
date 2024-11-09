import pandas as pd
import numpy as np

df = pd.read_csv('backend/original_data.csv', encoding='utf-16',low_memory=False)
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
    
columns_to_keep = ['eventName (actionDetails 1)', 'visitorType', 'visitCount', 'continent', 'country', 'visitIp']

df = df.loc[:, columns_to_keep]
df.sort_values(by='eventName (actionDetails 1)', inplace=True)
unique_event_names = df['eventName (actionDetails 1)'].nunique()
df.dropna(subset=['eventName (actionDetails 1)'], inplace=True)
df = df[~df['eventName (actionDetails 1)'].str.startswith('Initial')]
df = df[~df['eventName (actionDetails 1)'].str.startswith('Newsletter')]
df = df[~df['eventName (actionDetails 1)'].str.startswith('Accordion')]
df = df[~df['eventName (actionDetails 1)'].str.startswith('allgemein')]
df = df[~df['eventName (actionDetails 1)'].str.startswith('area')]
df = df[~df['eventName (actionDetails 1)'].str.startswith('city')]
df = df[~df['eventName (actionDetails 1)'].str.startswith('allgemein')]
df = df[df['eventName (actionDetails 1)'] != 'menschen']
df = df[df['eventName (actionDetails 1)'] != 'events']
df = df[df['eventName (actionDetails 1)'] != 'sommer']
df = df[df['eventName (actionDetails 1)'] != 'herbst']
df = df[df['eventName (actionDetails 1)'] != 'package_fuehrungen']
df = df[df['eventName (actionDetails 1)'] != 'poi']
#print(f"Number of unique event names: {unique_event_names}")
# unique_visit_ips = df['visitIp'].nunique()
# print(f"Number of unique visit IPs: {unique_visit_ips}")
# unique_countries = df['country'].nunique()
# print(f"Number of unique countries: {unique_countries}")
# print("Unique countries:")
# print(df['country'].unique())
# print("Updated DataFrame with only selected columns:")
# print(df)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*advent.*', 'adventmarkt', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(kuli|gastro).*', 'restaurant', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(hostel|hotel).*', 'hotel', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(gesundheit|krankenhaus).*', 'hospital', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(kultur).*', 'museum', regex=True)
df.to_csv('backend/prepared_data.csv', index=False)