import pandas as pd
import numpy as np

file_name = r"C:\Users\erikdn\Desktop\StomachDataSet2019128229177.csv"
"""
Script for plotting ratios of cod prey

Data: ICES Stomach Data
URL: http://ecosystemdata.ices.dk/stomachdata/download.aspx
"""


# Requires that single predator is pre-selected
stomach_data = pd.read_csv(file_name)

# Convert DataFrame to 2D list
all_prey = stomach_data.values.tolist()

# Get rows with herring as prey
herrings = stomach_data[stomach_data.Prey_LatinName == "Clupea harengus"]
# Convert DataFrame to 2D list
herrings = herrings.values.tolist()

# Get rows with sprat as prey
sprats = stomach_data[stomach_data.Prey_LatinName == "Sprattus sprattus"]
# Convert DataFrame to 2D list
sprats = sprats.values.tolist()

# Calculate total weight of prey in stomachs
# (45 is the index of 'Prey_Weight')
total_prey_weight_sum = 0
for k in all_prey:
    if not np.isnan(k[45]):
        total_prey_weight_sum += k[45]

# Calculate total weight of sprats found in stomachs
sprat_weight_sum = 0
for k in sprats:
    if not np.isnan(k[45]):
        sprat_weight_sum += k[45]

# Calculate total weight of herrings found in stomachs
herring_weight_sum = 0
for k in herrings:
    if not np.isnan(k[45]):
        herring_weight_sum += k[45]

print("Total:", total_prey_weight_sum)
print("Sprats:", sprat_weight_sum)
print("% sprat of total:", 100*sprat_weight_sum/total_prey_weight_sum)
print("Herrings", herring_weight_sum)
print("% herring of total:", 100*herring_weight_sum/total_prey_weight_sum)
