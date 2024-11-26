# PHBS-QPS-2024-Lu
#### This repository contains the code for fetching the US CPI data and calculating the inflation rate for the last four quarters (Q4 2023, Q1 2024, Q2 2024, and Q3 2024) using Python. The data is fetched from the Federal Reserve Economic Data (FRED) API, and the inflation rates are calculated based on the CPI values.
## Repository URL
#### https://github.com/Lynn-Lu09/phbs-qps-2024-Lu
## Setup and Running the Code
#### Follow these steps to set up the environment and run the code:
### 1. Clone the Repository
#### First, clone the repository to your local machine:
```python
git clone https://github.com/Lynn-Lu09/phbs-qps-2024-Lu
cd phbs-qps-2024
```
### 2. Set Up the Virtual Environment (Optional but Recommended)
#### It is recommended to use a virtual environment to manage your dependencies.
### 3. Install Dependencies
#### Make sure that the required Python libraries are installed. You can install the necessary libraries by running:
```python
pip install pandas_datareader
pip install pandas
pip install datetime
```
### 4. Running the Script
#### To fetch the CPI data and calculate the inflation rates for the last four quarters (Q4 2023, Q1 2024, Q2 2024, Q3 2024), run the following command:
```python
python scripts/fetch_cpi.py
```
#### This will execute the code in scripts/fetch_cpi.py, which calls the fetch_cpi_data() function from the src/data_fetcher.py file. The result will be displayed in the terminal, showing the inflation rates for the specified quarters.
### 5. Understanding the Code
#### - Data Fetching: The code uses the pandas_datareader library to fetch the CPI data from the FRED database.
#### - Quarterly Inflation Calculation: The data is resampled to quarterly data, and the inflation rates are calculated based on the year-over-year change in CPI.
#### - Handling Incomplete Quarters: If the current quarter is not complete (e.g., Q4 2024), the code will exclude it and only consider the latest complete quarter.
#### The script calculates inflation for the following quarters:
#### - 2023 Q4
#### - 2024 Q1
#### - 2024 Q2
#### - 2024 Q3
### 6. Files Structure
#### The project follows a common directory structure:
```python
phbs-qps-2024-Lu/
├── data/                    # Folder for storing any data files (if needed)
├── notebooks/           
├── scripts/                 # Folder containing scripts for data fetching and analysis
│   └── fetch_cpi.py         # Script to fetch CPI data and calculate inflation
├── src/                     # Folder for reusable Python functions
│   └── CPI_data_fetcher.py  # Function to fetch CPI data and calculate inflation
└── README.md                # This README file
```
## Summary of Changes to fetch_cpi_data() Function
#### - Data Fetching: The function fetches CPI data from FRED.
#### - Quarterly Resampling: Monthly CPI data is resampled to quarterly averages using .resample('Q').mean().
#### - Inflation Calculation: Quarterly inflation rates are calculated based on the quarter change in CPI (pct_change(periods=1)).
#### - Exclusion of Incomplete Quarters: If the current quarter is incomplete (like Q4 2024), the code will exclude the last quarter and use the latest full quarter's data.
### 7.  Example Output
#### When you run the script, it will display the CPI inflation rates for the following quarters:
```python
              Inflation
2023-12-31     0.674652
2024-03-31     0.938227
2024-06-30     0.697987
2024-09-30     0.304423
```

