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
    
columns_to_keep = ['eventName (actionDetails 1)', 'visitorType', 'visitCount', 'continent', 'country']

df = df.loc[:, columns_to_keep]
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
df = df[df['eventName (actionDetails 1)'] != 'fruehling']
df = df[df['eventName (actionDetails 1)'] != 'package_fuehrungen']
df = df[df['eventName (actionDetails 1)'] != 'poi']
df = df[df['eventName (actionDetails 1)'] != 'poi_verkehr']
df = df[df['eventName (actionDetails 1)'] != 'poi_bahnhof']
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
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(gesundheit|krankenhaus|poi_notdienste|poi_arzt_zahnarzt).*', 'hospital', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(kultur|poi_archaeologische_staette|poi_bildungseinrichtungen).*', 'museum', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(poi_badegewaesser|poi_hallenbad).*', 'swimming', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(poi_bauwerke_gebaeude|poi_natur-sehenswuerdigkeiten|poi_sehenswuerdigkeiten|poi_sonstige_natur-sehenswuerdigkeit|poi_aussichtswarte_aussichtspunkt_aussichtsturm).*', 'sehenswuerdigkeiten', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(poi_bekleidung_und_mode|poi_einkaufen).*', 'shopping', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(poi_parkmoeglichkeit_gratis|poi_parkmoeglichkeit_kostenpflichtig).*', 'parking', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(poi_tierpark_wildpark_zoo).*', 'zoo', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(radfahren_rennrad_e-bike|tour_rad-tour|tour_mountainbike-tour|mountainbiken).*', 'bike', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(poi_ausflugsschiff-fahrt_nostalgiebahnen|salzkammergut).*', 'trip', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(wandern_klettern_bergsport|tour_wanderweg).*', 'hike', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(poi_reitstall|reiten).*', 'horse riding', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'^event', 'activity', regex=True)
df['eventName (actionDetails 1)'] = df['eventName (actionDetails 1)'].str.replace(r'(?i).*(activity_vortraege|activity_vergnuegungsveranstaltung|activity_sonstige_vergnuegungsveranstaltung|activity_sonstige_tour|activity_sonstige_musikveranstaltung|activity_kurs|activity_konzert|activity_brauchtumsveranstaltung|activity_bauernmarkt|activity_ball_tanzveranstaltung).*', 'activity', regex=True)

df = df[~df['eventName (actionDetails 1)'].str.startswith('poi')]

df.sort_values(by='eventName (actionDetails 1)', inplace=True)
df.to_csv('backend/prepared_data.csv', index=False)

