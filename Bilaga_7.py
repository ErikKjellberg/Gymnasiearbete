import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Script for plotting stabilized values for sprat and cod

Data: VenSim simulation
"""


# Sprat data
sprat35 = "LOCAL FILE PATH"
sprat40 = "LOCAL FILE PATH"
sprat45 = "LOCAL FILE PATH"
sprat50 = "LOCAL FILE PATH"
sprat55 = "LOCAL FILE PATH"
sprat60 = "LOCAL FILE PATH"

# Cod data
cod35 = "LOCAL FILE PATH"
cod40 = "LOCAL FILE PATH"
cod45 = "LOCAL FILE PATH"
cod50 = "LOCAL FILE PATH"
cod55 = "LOCAL FILE PATH"
cod60 = "LOCAL FILE PATH"


def data_reader(filename, p):
    data = pd.read_excel(filename)
    array = np.array(data)[1:, 1:]
    y0 = array[:p, -1]
    x = [i*0.1 for i in range(len(y0))]
    return x, y0, array


sx35, sy035, sy35  = data_reader(sprat35, 85)
sx40, sy040, sy40  = data_reader(sprat40, 150)
sx45, sy045, sy45  = data_reader(sprat45, 150)
sx50, sy050, sy50  = data_reader(sprat50, 150)
sx55, sy055, sy55  = data_reader(sprat55, 150)
sx60, sy060, sy60  = data_reader(sprat60, 150)

cx35, cy035, cy35  = data_reader(cod35, 85)
cx40, cy040, cy40  = data_reader(cod40, 150)
cx45, cy045, cy45  = data_reader(cod45, 150)
cx50, cy050, cy50  = data_reader(cod50, 150)
cx55, cy055, cy55  = data_reader(cod55, 150)
cx60, cy060, cy60  = data_reader(cod60, 150)

# For the sprat
fig, (ax, b) = plt.subplots(1, 2)
p35, = ax.plot(sx35, sy035, label="R$_0$ = 3.5")
p40, = ax.plot(sx40, sy040, label="R$_0$ = 4.0")
p45, = ax.plot(sx45, sy045, label="R$_0$ = 4.5")
p50, = ax.plot(sx50, sy050, label="R$_0$ = 5.0")
p55, = ax.plot(sx55, sy055, label="R$_0$ = 5.5")
p60, = ax.plot(sx60, sy060, label="R$_0$ = 6.0")
ax.legend(loc='upper left')



# For the cod
c35, = b.plot(cx35, cy035, label="R$_0$ = 3.5")
c40, = b.plot(cx40, cy040, label="R$_0$ = 4.0")
c45, = b.plot(cx45, cy045, label="R$_0$ = 4.5")
c50, = b.plot(cx50, cy050, label="R$_0$ = 5.0")
c55, = b.plot(cx55, cy055, label="R$_0$ = 5.5")
c60, = b.plot(cx60, cy060, label="R$_0$ = 6.0")
b.legend(loc='upper left')

plt.ylabel('SSB (ton)')
plt.xlabel('N')
plt.show()
