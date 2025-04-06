# This script loads a dataset, displays basic information and a preview,
# calculates the number of observations and features, and checks for missing values.

import pandas as pd

# Load the dataset
file_path = 'Hotel Reservations.csv'
data = pd.read_csv(file_path)

# Display basic info and preview
df_hotel_reservations_info = data.info()
df_hotel_reservations_preview = data.head()

df_hotel_reservations_preview

# Get the number of observations and features
num_observations = data.shape[0]
num_features = data.shape[1]

print(f"\nNumber of observations: {num_observations}")
print(f"Number of features: {num_features}\n")

# Check for missing values in the dataset
missing_values_summary = data.isnull().sum()
missing_values_summary = missing_values_summary[missing_values_summary > 0]

if not missing_values_summary.empty:
    print(f"Number of missing values:\n{missing_values_summary}")
else:
    print("No missing values.")
