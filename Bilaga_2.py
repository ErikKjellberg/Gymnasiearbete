import matplotlib.pyplot as plt
from scipy import stats

"""
Script for plotting nutrients in the baltic sea between years 1950 and 1987

Data source: 
Eero et al. 2016. "Has eutrophication promoted forage fish production in the Baltic Sea?"
"""


nitrogen = [1.7, 1.9, 2.2, 2.1, 2.5, 2.8, 2.8, 3.25, 3.0, 3.6, 3.8, 3.8, 3.5, 3.9, 3.8, 4.8, 4.7, 4.8, 5.2, 4.8, 4.15, 4.4, 4.9, 4.5, 3.5, 4.5, 4.75, 4.3, 6.15, 5.8, 4.61, 5.13, 4.6, 5.2, 4.55, 4.7, 4.8, 4.4]

phosphorus = [0.2, 0.25, 0.22, 0.23, 0.26, 0.27, 0.25, 0.21, 0.2, 0.18, 0.32, 0.24, 0.26, 0.23, 0.27, 0.25, 0.32, 0.24, 0.36, 0.34, 0.4, 0.33, 0.48, 0.46, 0.51, 0.44, 0.56, 0.58, 0.74, 0.67, 0.72, 0.78, 0.68, 0.74, 0.68, 0.66, 0.75, 0.67]


slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(range(1950, 1988), [i[0]+i[1] for i in zip(map(lambda x: x*16, p), n)])
x = range(1950, 1988)
y = slope1*x+intercept1
print(slope1)


slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(range(1970, 1988), [i[0]+i[1] for i in zip(map(lambda x: x*16, p), n)][20:38])
x2 = range(1970, 1988)
y2 = slope2*x2+intercept2

# plotting n and p summed according to redfield ratio
plt.plot(range(1950, 1988), [i[0]+i[1] for i in zip(map(lambda x: x*16, p), n)])

# plotting between years 1950 and 1987
plt.plot(x,y)

# plotting between years 1970 and 1987
plt.plot(x2,y2)


plt.subplots_adjust(bottom=0.5)
plt.ylabel('')
plt.title('Summerad kväve och fosfor -- passad linje mellan 1950-1987')
#plt.show()
