import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import DataLoader

loader = DataLoader('BACKEND/prepared_data.csv')

x_train, x_test, y_train, y_test = loader.get_train_test_data()
data_frame = loader.get_dataframe()
features, target = loader.get_features_and_target()
#full_dataset = loader.get_full_dataset()

# Example can delete later 
print(x_train.head())
print(data_frame.head())