import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "hackathon\DGCA_DATA.csv"  # Update with your actual file path
df = pd.read_csv(file_path)

# Fix column name issues (strip any unwanted spaces)
df.columns = df.columns.str.strip()

# Create figure and axis
plt.figure(figsize=(12, 6))
sns.regplot(x=df["Avail Seats Km(millions)"], y=df["PAX load %"], 
            scatter_kws={'color':'blue', 'alpha': 0.7},  # Adjust transparency for better visibility
            line_kws={'color':'red', 'linewidth':2})  # Make the regression line more prominent

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.6)  # Dashed grid lines with some transparency

# Set title and labels with better font sizes
plt.title("Passenger Load Factor vs Available Seat Kilometers", fontsize=14, fontweight='bold')
plt.xlabel("Available Seat Kilometers (Millions)", fontsize=12)
plt.ylabel("Passenger Load Factor (%)", fontsize=12)

# Improve tick mark readability
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Show the plot
plt.show()
