import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate

class CollaborativeFiltering:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.data.rename(columns={'eventName (actionDetails 1)': 'eventName'}, inplace=True)
        self.reader = Reader(rating_scale=(1, 10))
        self.surprise_data = Dataset.load_from_df(self.data[['country', 'eventName', 'visitCount']], self.reader)
        self.svd = SVD()
        self.trainset, self.testset = train_test_split(self.surprise_data, test_size=0.2)
        self.cross_val_results = cross_validate(self.svd, self.surprise_data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
        self.svd.fit(self.trainset)

    def get_recommendations(self):
        unique_countries = self.data['country'].unique()
        all_events = self.data['eventName'].unique()
        recommendations_list = []

        for country in unique_countries:
            recommendations = []
            for event in all_events:
                est = self.svd.predict(uid=country, iid=event).est
                recommendations.append((event, est))
            
            recommendations.sort(key=lambda x: x[1], reverse=True)
            top_recommendations = recommendations[:5]

            for event, score in top_recommendations:
                recommendations_list.append({
                    'country': country,
                    'eventName': event,
                    'estimated_interest': score
                })

        return pd.DataFrame(recommendations_list)

    def save_recommendations(self, output_file):
        recommendations_df = self.get_recommendations()
        recommendations_df.to_csv(output_file, index=False)
        print(f"Recommendations have been saved to {output_file}")

# Example usage
if __name__ == '__main__':
    collab_filtering = CollaborativeFiltering('backend/prepared_data.csv')
    collab_filtering.save_recommendations('output.csv')
