# Import necessary libraries
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate
import random

# Load the data and rename columns for ease of use
data = pd.read_csv('backend/prepared_data.csv')
data.rename(columns={'eventName (actionDetails 1)': 'eventName'}, inplace=True)

# Check the distribution of each country
country_counts = data['country'].value_counts()
print("Initial distribution of countries:\n", country_counts)

# Find the maximum count of data points for any country to use as a target for balancing
max_count = country_counts.max()

# List to store new data points for underrepresented countries
new_data_points = []

# Generate synthetic data for minority countries
for country, count in country_counts.items():
    if count < max_count:
        # Calculate how many additional data points are needed
        additional_points = max_count - count
        for _ in range(additional_points):
            event = random.choice(data['eventName'].unique())
            visit_count = random.randint(1, 10)  # Randomly generate visitCount within the given rating scale
            new_data_points.append({'country': country, 'eventName': event, 'visitCount': visit_count})

# Convert the new data points to a DataFrame and append to the original data
synthetic_data = pd.DataFrame(new_data_points)
balanced_data = pd.concat([data, synthetic_data], ignore_index=True)

# Verify the new distribution
new_country_counts = balanced_data['country'].value_counts()
print("New distribution of countries:\n", new_country_counts)

# Define the Surprise Reader and dataset
reader = Reader(rating_scale=(1, 10))
surprise_data = Dataset.load_from_df(balanced_data[['country', 'eventName', 'visitCount']], reader)

# Train-test split
trainset, testset = train_test_split(surprise_data, test_size=0.2)

# Initialize and train the SVD model
svd = SVD()
cross_val_results = cross_validate(svd, surprise_data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
svd.fit(trainset)

# Get all unique countries and events for generating recommendations
unique_countries = balanced_data['country'].unique()
all_events = balanced_data['eventName'].unique()

# List to store recommendations for each country
recommendations_list = []

# Loop through each country to generate recommendations
for country in unique_countries:
    recommendations = []
    for event in all_events:
        # Predict the estimated interest for each event
        est = svd.predict(uid=country, iid=event).est
        recommendations.append((event, est))
    
    # Sort recommendations by estimated interest and store top 5 for each country
    recommendations.sort(key=lambda x: x[1], reverse=True)
    top_recommendations = recommendations[:5]
    
    # Append the recommendations for the current country to the list
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
    print()  # Blank line for readability

# Convert the recommendations list to a DataFrame
recommendations_df = pd.DataFrame(recommendations_list)

# Save the recommendations to a CSV file
recommendations_df.to_csv('backend/output.csv', index=False)
