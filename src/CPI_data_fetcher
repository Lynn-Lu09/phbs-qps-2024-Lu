import pandas_datareader.data as web
import pandas as pd
import datetime


def fetch_cpi_data():

    # Define the time range (since 2023 Q1)
    end_date = datetime.datetime.now()
    start_date = datetime.datetime(2023, 1, 1)  # Start from 2023 Q1

    # Fetch CPI data
    cpi = web.DataReader('CPIAUCSL', 'fred', start_date, end_date)

    # Resample monthly data to quarterly data by averaging the monthly values
    cpi_quarterly = cpi.resample('Q').mean()

    # Get the most recent full quarter. If we're in Q4 2024, we'll only consider Q3 2024.
    current_quarter = (end_date.month - 1) // 3 + 1
    if current_quarter == 4 and end_date.year == 2024:
        cpi_quarterly = cpi_quarterly[:'2024-09-30'] 
        
    # Select specific quarters: 2023 Q4, 2024 Q1, 2024 Q2, 2024 Q3
    selected_quarters = cpi_quarterly.loc[['2023-09-30', '2023-12-31', '2024-03-31', '2024-06-30', '2024-09-30']]

    # Calculate the quarterly inflation rates (year-over-year change)
    selected_quarters['Inflation'] = selected_quarters['CPIAUCSL'].pct_change(periods=1) * 100  # Convert to percentage

    return selected_quarters[['Inflation']].tail(4)

