import sys
sys.path.append('path/.../src')  # the path of "src" folder in your computer
import CPI_data_fetcher 
last_4_quarters = CPI_data_fetcher.fetch_cpi_data()
print(last_4_quarters)
