import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder

# Load your data
data = pd.read_csv('backend/prepared_data.csv')
data.rename(columns={'eventName (actionDetails 1)': 'eventName'}, inplace=True)

# Filter rows where the country count is below 2
country_counts = data['country'].value_counts()
countries_below_threshold = country_counts[country_counts < 2].index
filtered_data = data[data['country'].isin(countries_below_threshold)]

# Determine the unique event names for random assignment
unique_event_names = data['eventName'].unique()

# Function to create additional copies to meet a count of at least 4
def duplicate_with_random_event(df, count_needed=4):
    duplicates = []
    for _, row in df.iterrows():
        num_duplicates = max(0, count_needed - country_counts[row['country']])
        for _ in range(num_duplicates):
            new_row = row.copy()
            new_row['eventName'] = np.random.choice(unique_event_names)  # Random event name
            duplicates.append(new_row)
    return pd.DataFrame(duplicates)

# Create duplicates to ensure at least 4 occurrences per country
additional_data = duplicate_with_random_event(filtered_data)

# Merge the original data with the additional data
merged_data = pd.concat([data, additional_data], ignore_index=True)

# Save the merged data to a new CSV file
merged_data.to_csv('backend/merged_data.csv', index=False)

# Encode categorical columns
label_encoders = {}
for column in ['visitorType', 'continent', 'country']:
    le = LabelEncoder()
    merged_data[column] = le.fit_transform(merged_data[column])
    label_encoders[column] = le  # Store the encoder if you need to decode later

# Split the dataset into training and testing sets
train_data, test_data = train_test_split(merged_data, test_size=0.2, random_state=42, stratify=merged_data['country'])

# Separate features and target in the training data
X_train = train_data.drop(columns=['eventName'])
y_train = train_data['eventName']

# Apply SMOTE to balance the country distribution in the training set
smote = SMOTE(sampling_strategy='not majority', random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Combine resampled data into a DataFrame
train_resampled_data = pd.concat([X_train_resampled, y_train_resampled], axis=1)

# Verify the new distribution in the resampled training set
resampled_country_distribution = train_resampled_data['country'].value_counts(normalize=True) * 100
print("Resampled Country Distribution in Training Set:")
print(resampled_country_distribution)
