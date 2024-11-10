#%% import and loading data 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import DataLoader
import squarify

loader = DataLoader('BACKEND/prepared_data.csv')
x_train, x_test, y_train, y_test = loader.get_train_test_data()
data_frame = loader.get_dataframe()
features, target = loader.get_features_and_target()

#%%exploration of data 


#Austria vs other countries
## Load the data
#data = pd.read_csv('backend/prepared_data.csv')
#
## Separate Austria from other countries
#austria_data = data[data['country'] == 'Austria']
#other_countries_data = data[data['country'] != 'Austria']
#
## Aggregate visit counts for Austria and other countries
#austria_visit_counts = austria_data.groupby('eventName (actionDetails 1)')['visitCount'].sum().reset_index()
#other_countries_visit_counts = other_countries_data.groupby('country')['visitCount'].sum().reset_index()
#
#plt.figure(figsize=(14, 8))
#sns.barplot(x='eventName (actionDetails 1)', y='visitCount', data=austria_visit_counts, color='blue', label='Austria')
#sns.barplot(x='country', y='visitCount', data=other_countries_visit_counts, color='red', label='Other Countries')
#
#plt.title('Visit Counts: Austria vs Other Countries')
#plt.xlabel('Event Name / Country')
#plt.ylabel('Visit Count')
#plt.legend()
#plt.xticks(rotation=90)
#plt.show()

# pie chart of visitor types (very reasonable)
plt.figure(figsize=(8, 8), num=1)
data_frame['visitorType'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Proportion of Visitor Types')
plt.ylabel('')
plt.show()
plt.savefig('pie_chart_new_return.pdf', format='pdf')

## Bar Plot visitor types 
#plt.figure(figsize=(10, 6), num=2)   #reasonable but pie is nicer 
#sns.countplot(data=data_frame, x='visitorType')
#plt.title('Count of Visitor Types')
#plt.xlabel('Visitor Type')
#plt.ylabel('Count')
#plt.show()

# Scatter Plot visit count vs. target
plt.figure(figsize=(10, 6), num=2) #reasonable
plt.scatter(x=x_train['visitCount'], y=y_train)
plt.title('Visit Count vs. Target')
plt.xlabel('Visit Count')
plt.ylabel('Target')
plt.show()
plt.savefig('scatter_plot.pdf', format='pdf')

# cat plot of visit count by continent and visitor type (quite reasonable)
g = sns.catplot(data=data_frame, kind='bar', x='continent', y='visitCount', hue='visitorType', height=6, aspect=2)
g.set_axis_labels('Continent', 'Visit Count')
g.fig.suptitle('Visit Count by Continent and Visitor Type')
plt.show()

# treemap (fancy plot, midly reasonable)
grouped_data = data_frame.groupby(['country', 'visitorType']).size().reset_index(name='counts')
labels = [f"{row['country']} - {row['visitorType']}\n{row['counts']}" for index, row in grouped_data.iterrows()]
sizes = grouped_data['counts'].values
plt.figure(figsize=(16, 10))
squarify.plot(sizes=sizes, label=labels, alpha=0.8, color=sns.color_palette('pastel'))
plt.title('Treemap of Visitor Types by Country')
plt.axis('off')
plt.show()

# heatmap of visitor type by country (midly reasonable)
visitor_country_matrix = pd.crosstab(data_frame['country'], data_frame['visitorType'])
plt.figure(figsize=(14, 8))
sns.heatmap(visitor_country_matrix, annot=True, fmt='d', cmap='YlGnBu', linewidths=0.5)
plt.title('Visitor Type by Country')
plt.xlabel('Visitor Type')
plt.ylabel('Country')
plt.show()

# violin plot of visit count by continent (midly reasonable)
plt.figure(figsize=(12, 6))
sns.violinplot(data=data_frame, x='continent', y='visitCount', palette='muted')
plt.title('Visit Count by Continent')
plt.xlabel('Continent')
plt.ylabel('Visit Count')
plt.show()

# swarm plot of visit count by visitor type and continent (less reasonable)
plt.figure(figsize=(12, 6))
sns.swarmplot(data=data_frame, x='visitorType', y='visitCount', hue='continent', palette='Set2', dodge=True)
plt.title('Visit Count Distribution by Visitor Type and Continent')
plt.xlabel('Visitor Type')
plt.ylabel('Visit Count')
plt.legend(title='Continent')
plt.show()
