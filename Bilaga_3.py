import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
import numpy as np

"""
Script for plotting cod reproductive volume

Data source: 
Thorsten Blenckner
"""


file_name = r'C:\Users\erikdn\Pictures\GyA\Rudi s cod rv.xlsx'

stomach_data = pd.read_excel(file_name)

all_vals = stomach_data.values.tolist()

all_vals = [(i[0], i[3]) for i in all_vals]

# Linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress([i[0]-1970 for i in all_vals[0:20]], [i[1] for i in all_vals[0:20]])
print(r_value**2, p_value)
x = range(len(all_vals[0:20]))
y = slope*x+intercept




p = range(len(all_vals[0:20]))
plt.plot(range(len(all_vals)), [i[1] for i in all_vals])
plt.plot(x,y, label=f"r$^2$: {r_value**2:.4f}\np-val: {p_value:.4e}")
plt.legend(loc="upper right")
plt.xticks(range(len(all_vals)), list([v[0] if not i%5 else None for i, v in enumerate(all_vals)]), rotation=60, )
plt.subplots_adjust(bottom=0.5)
plt.ylabel(r'km$^3$')
plt.title('Reproductive volume -- passad linje mellan 1970-1990')
plt.show()
