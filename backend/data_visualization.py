import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import DataLoader

# Load the data
loader = DataLoader('BACKEND/prepared_data.csv')
x_train, x_test, y_train, y_test = loader.get_train_test_data()
data_frame = loader.get_dataframe()
features, target = loader.get_features_and_target()

# Histogram of Visit Count
plt.figure(figsize=(10, 6))
sns.histplot(data_frame['visitCount'], kde=True, bins=30)
plt.title('Distribution of Visit Count')
plt.xlabel('Visit Count')
plt.ylabel('Frequency')
plt.show()

# Bar Plot of Visitor Types
plt.figure(figsize=(10, 6))
sns.countplot(data=data_frame, x='visitorType')
plt.title('Count of Visitor Types')
plt.xlabel('Visitor Type')
plt.ylabel('Count')
plt.show()

# Box Plot of Visit Count by Visitor Type
plt.figure(figsize=(10, 6))
sns.boxplot(data=data_frame, x='visitorType', y='visitCount')
plt.title('Visit Count by Visitor Type')
plt.xlabel('Visitor Type')
plt.ylabel('Visit Count')
plt.show()

# Scatter Plot of Visit Count vs. Target
plt.figure(figsize=(10, 6))
plt.scatter(x=x_train['visitCount'], y=y_train)
plt.title('Visit Count vs. Target')
plt.xlabel('Visit Count')
plt.ylabel('Target')
plt.show()

# Heatmap of Correlation Matrix
plt.figure(figsize=(12, 8))
correlation_matrix = data_frame.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

