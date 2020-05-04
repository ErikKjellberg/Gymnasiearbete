import pandas as pd
from statistics import mean

"""
Script for extracting data of nutrients levels in Baltic sea

Data source: ICES Oceanography
URL: http://www.ices.dk/marine-data/data-portals/Pages/ocean.aspx
"""


# Data from ICES
file_name = r"C:\Users\mathiasbn\Desktop\GyA\Sverige2016-2020.csv"

# Stores nutrient data in pandas data frame
nutrient_data = pd.read_csv(file_name)

# Extracts total phosphorus from data frame
TPHS = nutrient_data.loc[:, "TPHS [umol/l]"]

# Mean value
print(mean(TPHS))
