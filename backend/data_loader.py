import pandas as pd
from sklearn.model_selection import train_test_split
from surprise import Dataset, Reader

class DataLoader:
    def __init__(self, file_path, encoding='utf-8', line_format='user item rating', sep=','):
        self.data = pd.read_csv(file_path, encoding=encoding)
        reader = Reader(line_format=line_format, sep=sep)
        # Ensure only the necessary columns are passed to Dataset.load_from_df
        #self.surprise_data = Dataset.load_from_df(self.data[['pageTitle (actionDetails 0)','visitorType', 'visitCount', 'continent', 'country']], reader)
        self.df = self.data.drop('eventName (actionDetails 1)', axis=1) 
        self.target = self.data['eventName (actionDetails 1)']
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.df, self.target, test_size=0.2)

    def get_train_test_data(self):
        return self.x_train, self.x_test, self.y_train, self.y_test

    def get_dataframe(self):
        return self.data

    
    def get_features_and_target(self):
    
        return self.df, self.target
    
    #def get_full_dataset(self):
    #
    #    return self.surprise_data


#example 
if __name__ == '__main__':
    loader = DataLoader('BACKEND/prepared_data.csv')
    x_train, x_test, y_train, y_test = loader.get_train_test_data()
    data_frame = loader.get_dataframe()
    features, target = loader.get_features_and_target()
    #full_dataset = loader.get_full_dataset()

    print(x_train.head())
    print(data_frame.head())
    print(features.head())
    print(target.head())