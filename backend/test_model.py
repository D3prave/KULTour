# Import necessary libraries
import pandas as pd
from sdv.tabular import CTGAN
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate

# Load the data and rename columns for ease of use
data = pd.read_csv('backend/prepared_data.csv')
data.rename(columns={'eventName (actionDetails 1)': 'eventName'}, inplace=True)

# Identify underrepresented countries (classes) based on visit counts
country_counts = data['country'].value_counts()
underrepresented_countries = country_counts[country_counts < 5].index

# Separate data into underrepresented and well-represented classes
underrepresented_data = data[data['country'].isin(underrepresented_countries)]
well_represented_data = data[~data['country'].isin(underrepresented_countries)]

# Initialize and train the CTGAN model on underrepresented data only
ctgan = CTGAN(epochs=300)
ctgan.fit(underrepresented_data[['country', 'eventName', 'visitCount']])

# Generate synthetic data for underrepresented classes
# Generate a specific number of samples to balance the dataset (e.g., 1000)
synthetic_data = ctgan.sample(1000)

# Combine well-represented original data with new synthetic data
augmented_data = pd.concat([well_represented_data, synthetic_data], ignore_index=True)

# Define the Surprise Reader and dataset with augmented data
reader = Reader(rating_scale=(1, 10))
surprise_data = Dataset.load_from_df(augmented_data[['country', 'eventName', 'visitCount']], reader)

# Train-test split
trainset, testset = train_test_split(surprise_data, test_size=0.2)

# Initialize and train the SVD model
svd = SVD()
cross_val_results = cross_validate(svd, surprise_data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
svd.fit(trainset)

# Get all unique countries and events for generating recommendations
unique_countries = augmented_data['country'].unique()
all_events = augmented_data['eventName'].unique()

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

# Convert the recommendations list to a DataFrame
recommendations_df = pd.DataFrame(recommendations_list)

# Save the recommendations to a CSV file
recommendations_df.to_csv('output.csv', index=False)

print("Recommendations have been saved to output.csv")
