import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset (Replace 'your_file.csv' with actual file path)
df = pd.read_csv("hackathon\DGCA_DATA.csv")

# Convert 'Month' column to datetime format (if applicable)
df['Month'] = pd.to_datetime(df['Month'])

# Sort values by Month to ensure proper time series visualization
df = df.sort_values(by='Month')

# Plot the Weight Load Factor (%) over time
plt.figure(figsize=(14, 6))
plt.plot(df['Month'], df['Weight Load Factor %'], marker='o', linestyle='-', color='b', label='Weight Load Factor (%)')

# Add grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add title and labels
plt.title("Fluctuation of Weight Load Factor (%) Over Time", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Weight Load Factor (%)", fontsize=12)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.show()
