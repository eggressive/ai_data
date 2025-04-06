import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# This dataset contains a list of video game sales from 1980 to 2016, including information such as:
# - Name of the game
# - Platform
# - Year of release
# - Genre
# - Publisher
# - Sales in different regions (NA, EU, JP, and others)
# - Global sales
# Source: https://www.kaggle.com/datasets/thedevastator/global-video-game-sales

# Load the dataset
file_path = "datasets/C1M2_vgsales_2010_50.csv"
vg_sales_df = pd.read_csv(file_path)

# Remove the first two rows which are not part of the data
vg_sales_cleaned = vg_sales_df.iloc[2:].reset_index(drop=True)
# Set the correct headers using the second row (originally index 1)
vg_sales_cleaned.columns = [
    'Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher',
    'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'
]
# Convert numeric columns to appropriate types
numeric_columns = ['Rank', 'Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
for col in numeric_columns:
    vg_sales_cleaned[col] = pd.to_numeric(vg_sales_cleaned[col], errors='coerce')

# Display cleaned dataset info
print(vg_sales_cleaned.head())
vg_sales_cleaned.info(), vg_sales_cleaned.head()

# Display the top 10 games by Global Sales
top_10_global_sales = vg_sales_cleaned.sort_values(by="Global_Sales", ascending=False).head(10)
print("\nTop 10 Games by Global Sales:")
print(top_10_global_sales)

# Plotting the top 10 games by Global Sales
plt.figure(figsize=(12, 6))
sns.barplot(x='Global_Sales', y='Name', data=top_10_global_sales, palette='pastel', hue='Name', legend=False)
plt.title('Top 10 Games by Global Sales')
plt.xlabel('Global Sales (in millions)')
plt.ylabel('Game Name')
plt.tight_layout()  # Ensure the layout adjusts to prevent cutting
os.makedirs('plot', exist_ok=True)
plt.savefig('plot/top_10_global_sales.png')
print("\nPlot of top 10 games by global sales saved as 'plot/top_10_global_sales.png'")

# Count of games per Genre (category)
genre_counts = vg_sales_cleaned['Genre'].value_counts().reset_index()
genre_counts.columns = ['Genre', 'Game_Count']

print("\nCount of Games per Genre:")
print(genre_counts)

# Plotting the count of games per Genre
plt.figure(figsize=(12, 6))
sns.barplot(x='Game_Count', y='Genre', data=genre_counts, palette='pastel', hue='Genre', legend=False)
plt.title('Count of Games per Genre')
plt.xlabel('Number of Games')
plt.ylabel('Genre')
os.makedirs('plot', exist_ok=True)
plt.savefig('plot/game_count.png')
print ("\nPlot of game count per genre saved as 'plot/game_count.png'")

# Grouping by Year to analyze sales trends over time
sales_by_year = vg_sales_cleaned.groupby('Year').agg({
    'Global_Sales': ['sum', 'mean'],
    'NA_Sales': 'sum',
    'EU_Sales': 'sum',
    'JP_Sales': 'sum',
    'Other_Sales': 'sum'
}).reset_index()

# Flatten MultiIndex columns
sales_by_year.columns = ['Year', 'Total_Global_Sales', 'Avg_Global_Sales', 
                         'Total_NA_Sales', 'Total_EU_Sales', 'Total_JP_Sales', 'Total_Other_Sales']
print("\nSales by Year:")
print(sales_by_year.head())
# Plotting sales trends over the years
plt.figure(figsize=(14, 8))
sns.lineplot(data=sales_by_year, x='Year', y='Total_Global_Sales', label='Total Global Sales', color='blue')
sns.lineplot(data=sales_by_year, x='Year', y='Total_NA_Sales', label='Total NA Sales', color='orange')
sns.lineplot(data=sales_by_year, x='Year', y='Total_EU_Sales', label='Total EU Sales', color='green')
sns.lineplot(data=sales_by_year, x='Year', y='Total_JP_Sales', label='Total JP Sales', color='red')
sns.lineplot(data=sales_by_year, x='Year', y='Total_Other_Sales', label='Total Other Sales', color='purple')
plt.title('Video Game Sales Trends Over the Years')
plt.xlabel('Year')
plt.ylabel('Sales (in millions)')
plt.legend()
plt.tight_layout()
os.makedirs('plot', exist_ok=True)
plt.savefig('plot/sales_trends_over_years.png')
print("\nPlot of video game sales trends over the years saved as 'plot/sales_trends_over_years.png'\n")

# Calculate the sum of Global Sales for the first 10 games
top_10_global_sales_sum = vg_sales_cleaned.head(10)['Global_Sales'].sum()
print(f"Sum of Global Sales for the Top 10 Games: {top_10_global_sales_sum:.2f} million\n")

# Extract the 'Year' from the first 10 games and calculate the range
first_10_years = vg_sales_cleaned.head(10)['Year']
year_range = first_10_years.max() - first_10_years.min()
print(f"Year Range for the First 10 Games: {year_range} years\n")
