#%% imports 
#general/ data visualization
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_validate
from surprise import Dataset, Reader, SVD



#%% loading the data 
data = Dataset.load_from_df(pd.read_csv('new_data.csv', encoding='utf-16'), Reader(line_format='user item rating', sep=','))
x = data.drop('rating', axis=1) # adjust the target column -> page title
y = data['rating']  
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#%% data visualization 



#%% training using SVD 
algo = SVD()
pipe
cross_validate(algo, data_train, measures=['RMSE', 'MAE'], cv=3, verbose=True)

# Fit the model on the full dataset
trainset = data.build_full_trainset()
algo.fit(data_train)

# Example prediction for a user and location
user_id = 'user1'
location_id = 'location1'
prediction = algo.predict(user_id, location_id)
print(prediction)
