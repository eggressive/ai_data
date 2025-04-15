import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load the dataset
file_path = "datasets/Copy of C1M2_PracticeLab_3_Exploring_Baby_Names - Data.csv"
baby_names_df = pd.read_csv(file_path)

# Display the first few rows to understand the structure
# print(baby_names_df.head())

# Filter dataset for the last 50 years (1973–2022)
filtered_df = baby_names_df[baby_names_df['Year'] >= 1973]

# Separate by sex
female_names = filtered_df[filtered_df['Sex'] == 'F']
male_names = filtered_df[filtered_df['Sex'] == 'M']

# Aggregate total counts over 50 years for each name
top_female_names = female_names.groupby('Name')['Count'].sum().nlargest(20)
top_male_names = male_names.groupby('Name')['Count'].sum().nlargest(20)

# Display the top 10 baby names by gender
print("Top 10 Female Names by Total Count:\n", top_female_names.head(10))
print("Top 10 Male Names by Total Count:\n", top_male_names.head(10))

# Sum the total count for each unique name over all years
unique_name_counts = baby_names_df.groupby('Name')['Count'].sum().reset_index()

# Sort by count in descending order to see which names are most common
unique_name_counts_sorted = unique_name_counts.sort_values(by='Count', ascending=False)
# print("Unique Name Counts:\n", unique_name_counts_sorted)

# Count the number of unique baby names in the entire dataset
num_unique_names = baby_names_df['Name'].nunique()
num_unique_names
print(f"\nTotal number of unique baby names in the dataset: {num_unique_names}")

# Filter last 50 years for male and female names separately
last_50_female = baby_names_df[(baby_names_df['Year'] >= 1973) & (baby_names_df['Sex'] == 'F')]
last_50_male = baby_names_df[(baby_names_df['Year'] >= 1973) & (baby_names_df['Sex'] == 'M')]

# Aggregate total counts by name
female_name_totals = last_50_female.groupby('Name')['Count'].sum().sort_values(ascending=False).head(20)
male_name_totals = last_50_male.groupby('Name')['Count'].sum().sort_values(ascending=False).head(20)

# Calculate total births covered by top 20 names
total_female_top20 = female_name_totals.sum()
total_male_top20 = male_name_totals.sum()

print(f"Total births covered by top 20 female names: {total_female_top20}")
print(f"Total births covered by top 20 male names: {total_male_top20}")

# Prepare data: top 40 names by total count
top_40_names = unique_name_counts.sort_values(by='Count', ascending=False).head(40)

# Create histogram for the top 40 names
plt.figure(figsize=(14, 7))
bars = plt.bar(top_40_names['Name'], top_40_names['Count'], color='plum', alpha=0.6)
plt.xticks(rotation=90)
plt.ylabel('Count')
plt.xlabel('Unique names')
plt.title('Popularity of unique names')
# Format y-axis to show full numbers
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('plot/unique_names.png')
print("\nPlot histogram for the top 40 names saved as 'plot/unique_names.png'")
