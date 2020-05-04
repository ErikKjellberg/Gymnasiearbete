import pandas as pd

"""
Script for extracting data of nutrient levels in Baltic Sea

Data: ICES Oceanography
URL: http://www.ices.dk/marine-data/data-portals/Pages/ocean.aspx
"""

# Data from ICES
file_name = r"C:\Users\mathiasbn\Desktop\GyA\1990.csv"

# Stores nutrient data in pandas Data Frame
nutrient_data = pd.read_csv(file_name)

# Handles special cases where values are stored as strings in csv-file
TPHS = [float(element) for element in nutrient_data.loc[:, "TPHS [umol/l]"] if '<' not in element]

# Mean value
print(sum(TPHS) / len(TPHS))