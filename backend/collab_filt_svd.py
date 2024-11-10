import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate
import random

class CollaborativeFiltering:
    def __init__(self, file_path, first_time_visitor=False):
        self.data = pd.read_csv(file_path)
        self.data.rename(columns={'eventName (actionDetails 1)': 'eventName'}, inplace=True)
        self.balance_data() #underrepresented countries
        self.reader = Reader(rating_scale=(1, 10))
        self.surprise_data = Dataset.load_from_df(self.balanced_data[['country', 'eventName', 'visitCount']], self.reader)
        
        # train-test , SVD , Cross_val
        self.trainset, self.testset = train_test_split(self.surprise_data, test_size=0.2)
        self.svd = SVD()
        self.cross_val_results = cross_validate(self.svd, self.surprise_data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
        self.svd.fit(self.trainset)

        # Allowed categories for first-time visitors
        self.allowed_categories = ["HOTEL", "RESTAURANT", "MUSEUM", "ATTRACTIONS"]
        self.first_time_visitor = first_time_visitor

    def balance_data(self):
        country_counts = self.data['country'].value_counts()
        print("Initial distribution of countries:\n", country_counts) #distribution of countries

        max_count = country_counts.max() # Maximum count of any country
        new_data_points = [] #list for synthetic data

        # Generate synthetic data for minority countries
        for country, count in country_counts.items():
            if count < max_count:
                # Calculate how many additional data points are needed
                additional_points = max_count - count
                for _ in range(additional_points):
                    event = random.choice(self.data['eventName'].unique())
                    visit_count = random.randint(1, 10)  # Randomly generate visitCount within the given rating scale
                    new_data_points.append({'country': country, 'eventName': event, 'visitCount': visit_count})

        # Convert the new data points to a DataFrame and append to the original data
        synthetic_data = pd.DataFrame(new_data_points)
        self.balanced_data = pd.concat([self.data, synthetic_data], ignore_index=True)

        # Verify the new distribution
        new_country_counts = self.balanced_data['country'].value_counts()
        print("New distribution of countries:\n", new_country_counts)

    def get_recommendations(self):
        unique_countries = self.balanced_data['country'].unique()
        all_events = self.balanced_data['eventName'].unique()
        recommendations_list = []

        for country in unique_countries:
            recommendations = []
            for event in all_events:
                # Filter events based on allowed categories if the visitor is a first-time visitor
                if self.first_time_visitor:
                    # Check if the event belongs to one of the allowed categories for first-timers
                    if not any(category in event.upper() for category in self.allowed_categories):
                        continue

                # Predict
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
        
            # Print the recommendations for the current country
            print(f"Top recommendations for {country}:")
            for event, score in top_recommendations:
                print(f"  Event: {event}, Estimated Interest: {score:.2f}")
            print()  # Readability

        return pd.DataFrame(recommendations_list)

    def save_recommendations(self, output_file):
        recommendations_df = self.get_recommendations()
        recommendations_df.to_csv(output_file, index=False)
        print(f"Recommendations have been saved to {output_file}")
        
# Usage
#collab_filtering = CollaborativeFiltering('backend/prepared_data.csv')
#collab_filtering.get_recommendations()
#collab_filtering.save_recommendations('recommendations.csv')
