import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_flight_departures(df):
    """Plots the trend of flight departures over time."""
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Month', y='No. Departure (AF)', marker='o', color='b', linewidth=2)

    plt.title('Trend of Flight Departures Over Time', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Departures', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def plot_pax_load_vs_seat_kms(df):
    """Plots the relationship between Passenger Load Factor and Available Seat Kilometers."""
    plt.figure(figsize=(12, 6))
    sns.regplot(x=df["Avail Seats Km(millions)"], y=df["PAX load %"], 
                scatter_kws={'color':'blue', 'alpha': 0.7},  
                line_kws={'color':'red', 'linewidth':2})  

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title("Passenger Load Factor vs Available Seat Kilometers", fontsize=14, fontweight='bold')
    plt.xlabel("Available Seat Kilometers (Millions)", fontsize=12)
    plt.ylabel("Passenger Load Factor (%)", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()


def plot_weight_load_factor(df):
    """Plots the fluctuation of Weight Load Factor over time."""
    plt.figure(figsize=(14, 6))
    plt.plot(df['Month'], df['Weight Load Factor %'], marker='o', linestyle='-', color='b', label='Weight Load Factor (%)')

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title("Fluctuation of Weight Load Factor (%) Over Time", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Weight Load Factor (%)", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()



# Load the dataset
df = pd.read_csv('Hackathon\DGCA_DATA.csv')

# Convert 'Month' to datetime format
df['Month'] = pd.to_datetime(df['Month'], format='%m/%Y')
df = df.sort_values('Month')
df = df.dropna()

def load_data():
    df = pd.read_csv('Hackathon/DGCA_DATA.csv')
    df['Month'] = pd.to_datetime(df['Month'], format='%m/%Y')
    df = df.sort_values('Month').dropna()
    return df

def display_menu():
    print("\nAviation Data Analysis Menu:")
    print("1. Plot Flight Departures Over Time")
    print("2. Plot Passenger Load Factor vs Available Seat Kilometers")
    print("3. Plot Weight Load Factor Over Time")

def main():
    df = load_data()
    while True:
        display_menu()
        choice = input("Enter your choice (0-3): ")
        
        match choice:
            case '1':
                plot_flight_departures(df)
            case '2':
                plot_pax_load_vs_seat_kms(df)
            case '3':
                plot_weight_load_factor(df)
            case '0':
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please select a number between 0 and 3.")

if __name__ == "__main__":
    main()
           
            








