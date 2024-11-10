#%% import and loading data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from data_loader import DataLoader
import squarify

# Ensure the 'BACKEND/PDF' directory exists
pdf_path = 'BACKEND/PDF'
if not os.path.exists(pdf_path):
    os.makedirs(pdf_path)

# Load the data
loader = DataLoader('BACKEND/prepared_data.csv')
x_train, x_test, y_train, y_test = loader.get_train_test_data()
data_frame = loader.get_dataframe()
features, target = loader.get_features_and_target()

#%% exploration of data 

# Pie chart of visitor types (very reasonable)
plt.figure(figsize=(8, 8))
data_frame['visitorType'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Proportion of Visitor Types')
plt.ylabel('')
plt.savefig(f'{pdf_path}/pie_chart_visitor_types.pdf', format='pdf')
plt.show()

# Scatter Plot visit count vs. target
plt.figure(figsize=(10, 6))
plt.scatter(x=x_train['visitCount'], y=y_train)
plt.title('Visit Count vs. Target')
plt.xlabel('Visit Count')
plt.ylabel('Target')
plt.savefig(f'{pdf_path}/scatter_plot_visit_count_vs_target.pdf', format='pdf')
plt.show()

# Cat plot of visit count by continent and visitor type (quite reasonable)
g = sns.catplot(data=data_frame, kind='bar', x='continent', y='visitCount', hue='visitorType', height=6, aspect=2)
g.set_axis_labels('Continent', 'Visit Count')
g.fig.suptitle('Visit Count by Continent and Visitor Type')
g.savefig(f'{pdf_path}/cat_plot_visit_count_by_continent_and_visitor_type.pdf', format='pdf')
plt.show()

# Treemap (fancy plot, mildly reasonable)
grouped_data = data_frame.groupby(['country', 'visitorType']).size().reset_index(name='counts')
labels = [f"{row['country']} - {row['visitorType']}\n{row['counts']}" for index, row in grouped_data.iterrows()]
sizes = grouped_data['counts'].values
plt.figure(figsize=(16, 10))
squarify.plot(sizes=sizes, label=labels, alpha=0.8, color=sns.color_palette('pastel'))
plt.title('Treemap of Visitor Types by Country')
plt.axis('off')
plt.savefig(f'{pdf_path}/treemap_visitor_types_by_country.pdf', format='pdf')
plt.show()

# Heatmap of visitor type by country (mildly reasonable)
visitor_country_matrix = pd.crosstab(data_frame['country'], data_frame['visitorType'])
plt.figure(figsize=(14, 8))
sns.heatmap(visitor_country_matrix, annot=True, fmt='d', cmap='YlGnBu', linewidths=0.5)
plt.title('Visitor Type by Country')
plt.xlabel('Visitor Type')
plt.ylabel('Country')
plt.savefig(f'{pdf_path}/heatmap_visitor_type_by_country.pdf', format='pdf')
plt.show()

# Violin plot of visit count by continent (mildly reasonable)
plt.figure(figsize=(12, 6))
sns.violinplot(data=data_frame, x='continent', y='visitCount', palette='muted')
plt.title('Visit Count by Continent')
plt.xlabel('Continent')
plt.ylabel('Visit Count')
plt.savefig(f'{pdf_path}/violin_plot_visit_count_by_continent.pdf', format='pdf')
plt.show()

# Swarm plot of visit count by visitor type and continent (less reasonable)
plt.figure(figsize=(12, 6))
sns.swarmplot(data=data_frame, x='visitorType', y='visitCount', hue='continent', palette='Set2', dodge=True)
plt.title('Visit Count Distribution by Visitor Type and Continent')
plt.xlabel('Visitor Type')
plt.ylabel('Visit Count')
plt.legend(title='Continent')
plt.savefig(f'{pdf_path}/swarm_plot_visit_count_by_visitor_type_and_continent.pdf', format='pdf')
plt.show()