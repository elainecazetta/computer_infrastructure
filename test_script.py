# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import os

def plot_data():
    """
    Opens the latest CSV file in the 'data' folder, plots the 
    closing prices of the FAANG companies, and saves the plot 
    with a timestamped filename in the 'plots' folder.
    """

    # List and sort files
    files = os.listdir("data/")
    files.sort(reverse=True)

    # Latest file (newest timestamp)
    latest = files[0]
    full_path = os.path.join("data", latest)

    print(f"Using latest file: {full_path}")

    # Read the CSV with multi-level columns
    df = pd.read_csv(full_path, header=[0, 1], index_col=0)

    # Convert index to datetime
    df.index = pd.to_datetime(df.index)

    # Select only Close prices
    close_df = df["Close"]

    # Title date based on filename
    base = latest.replace(".csv", "")
    title_date = dt.datetime.strptime(base, "%Y%m%d-%H%M%S").strftime("%Y-%m-%d %H:%M:%S")

    # Plot
    close_df.plot(figsize=(10, 6), title=f"FAANG Closing Prices - {title_date}")
    plt.xlabel("Date and Time")
    plt.ylabel("Price (USD)")
    plt.legend(title="Company")

    # Save plot
    plot_filename = f"plots/{dt.datetime.now().strftime('%Y%m%d-%H%M%S')}.png"
    plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
    plt.show()

    print(f"Plot saved as: {plot_filename}")

# Example usage
plot_data()