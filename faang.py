#! usr/bin/env python

# Ref: https://chatgpt.com/share/693c9149-8a6c-8007-94a1-66c6694c9382

    # -------------------------
    # get_data() script
    # -------------------------

def get_data():
    # References: 
    # https://www.w3schools.com/python/python_functions.asp
    # https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    # https://www.w3schools.com/python/python_functions.asp
    # https://www.geeksforgeeks.org/python/python-def-keyword/
    # OpenAI
    """
    Downloads hourly stock data for the previous five days 
    for the FAANG companies and saves it as a timestamped CSV file.
    """
        
    # Import libraries inside the function
    import yfinance as yf
    import datetime as dt
    import os
      
    # Download hourly data for the last 5 days of FAANG tickers
    df = yf.download(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG'], period='5d', interval='1h')

    # Create 'data' folder if it doesn't exist
    # Ref: https://docs.python.org/3/library/os.html
    # Ref: OpenAI
    os.makedirs("data", exist_ok=True)

    # Generate filename with timestamp
    filename = "data/" + dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"

    # Save data to CSV
    df.to_csv(filename)

    # Print confirmation message
    print(f"Data saved to {filename}")

    # Return the downloaded DataFrame
    return df

    # -------------------------
    # plot_data() script
    # -------------------------

def plot_data():
    # References:
    # https://matplotlib.org/stable/gallery/index.html
    # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
    # https://docs.python.org/3/library/os.html
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
    # OpenAI
    """
    Opens the latest CSV file in the 'data' folder, plots the 
    closing prices of the FAANG companies, and saves the plot 
    with a timestamped filename in the 'plots' folder.
    """

    import os
    import pandas as pd
    import datetime as dt
    import matplotlib.pyplot as plt

    # List and sort files
    files = os.listdir("data/")
    files.sort(reverse=True) # Newest file first

    # Latest file
    latest = files[0] # Get the latest file
    full_path = os.path.join("data", latest) # Get full path

    print(f"Using latest file: {full_path}")

    # Read the CSV with multi-level columns
    df = pd.read_csv(full_path, header=[0, 1], index_col=0, parse_dates=True)

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

    # -------------------------
    # Run both
    # -------------------------
get_data()
plot_data()


    
