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