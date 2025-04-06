# This script loads a hotel reservations dataset, displays basic information and a preview,
# calculates the number of observations and features, checks for missing values,
# verifies chronological order of observations, analyzes the range of 'no_of_children',
# visualizes its distribution, and evaluates lead time for bookings with corresponding plots.

# This dataset contains hotel reservations data, including features such as:
# - Booking details (arrival date, lead time, number of children, etc.)
# - Customer behavior (repeated guest, previous cancellations, etc.)
# - Room preferences and special requests
# The dataset is useful for classification tasks and predictive modeling.
# Source: https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
file_path = 'datasets/Hotel Reservations.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

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
    print("No missing values.\n")

# Check if the observations are in chronological order based on arrival date (year, month, day)
df_sorted_check = data.sort_values(
    by=["arrival_year", "arrival_month", "arrival_date"]
).reset_index(drop=True)

# Compare the original with the sorted one to see if they match
is_chronological = data.equals(df_sorted_check)

if is_chronological:
    print("Observations are in chronological order.\n")
else:
    print("Observations are not in chronological order.\n")

# Get the minimum and maximum values for the 'no_of_children' feature
children_min = data["no_of_children"].min()
children_max = data["no_of_children"].max()

print(f"Range of 'no_of_children': {children_min} to {children_max}\n")

# Plot a histogram to visualize the distribution of 'no_of_children'
plt.figure(figsize=(10, 6))
plt.hist(data["no_of_children"], bins=range(0, 12), edgecolor='black')
plt.title("Distribution of Number of Children per Booking")
plt.xlabel("Number of Children")
plt.ylabel("Number of Bookings")
plt.xticks(range(0, 11))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
os.makedirs('plot', exist_ok=True)
plt.savefig('plot/no_of_children.png')
print("Plot of 'no_of_children' distribution saved as 'plot/no_of_children.png'\n")

# Calculate the number and percentage of bookings made at least one month (30 days) in advance
at_least_one_month = data[data["lead_time"] >= 30]
percent_one_month_advance = (len(at_least_one_month) / len(data)) * 100
print(f"Bookings made at least one month (30 days) in advance: {len(at_least_one_month)}")
print(f"Percentage of bookings made at least one month (30 days) in advance: {percent_one_month_advance:.2f}%\n")

# Plot a pie chart to visualize the percentage
labels = ['≥ 30 Days in Advance', '< 30 Days in Advance']
sizes = [percent_one_month_advance, 100 - percent_one_month_advance]

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, explode=(0.05, 0))
plt.title("Percentage of Bookings Made At Least One Month in Advance")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.savefig('plot/lead_time.png')
print("Plot of Percentage of Bookings Made At Least One Month in Advance saved as 'plot/lead_time.png'\n")
