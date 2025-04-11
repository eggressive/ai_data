import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded baby names dataset
file_path = "datasets/Copy of C1M2_Demo_10_Baby_names - Sheet1.csv"
df = pd.read_csv(file_path)

# Display the first few rows to understand its structure
# print(df.head())

# Filter for the name "Ruby"
ruby_df = df[df['Name'].str.lower() == 'ruby']

# Group by year, summing both male and female counts
ruby_total_yearly = ruby_df.groupby('Year')['Count'].sum()

# Calculate 10-year moving average
ruby_moving_avg = ruby_total_yearly.rolling(window=10).mean()

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(ruby_total_yearly.index, ruby_total_yearly.values, label='Annual Count', marker='o')
plt.plot(ruby_moving_avg.index, ruby_moving_avg.values, label='10-Year Moving Average', linestyle='--', linewidth=2)
plt.title('Popularity of the Name "Ruby" Over the Years with 10-Year Moving Average')
plt.xlabel('Year')
plt.ylabel('Total Number of Babies Named Ruby')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plot/ruby.png')
print("\nPlot of popularity of the name \"Ruby\" over the years saved as 'plot/top_10_global_sales.png'")
