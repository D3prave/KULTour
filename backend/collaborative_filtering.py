#%% imports 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_validate
from surprise import Dataset, Reader, SVD
from data_loader import DataLoader

loader = DataLoader('BACKEND/prepared_data.csv')

x_train, x_test, y_train, y_test = loader.get_train_test_data()
data_frame = loader.get_dataframe()
features, target = loader.get_features_and_target()
#full_dataset = loader.get_full_dataset()

# Example can delete later 
print(x_train.head())
print(data_frame.head())



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
