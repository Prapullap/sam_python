import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "hackathon\DGCA_DATA.csv"
df = pd.read_csv(file_path)

# Convert 'Month' to datetime format
df['Month'] = pd.to_datetime(df['Month'], format='%m/%Y')

# Sort data by date
df = df.sort_values(by='Month')

# Plot the trend of flight departures over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Month', y='No. Departure (AF)', marker='o', color='b', linewidth=2)

# Customize the plot
plt.title('Trend of Flight Departures Over Time', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Departures', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.show()
