import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# generating a uniform background(base) between a 110 GeV and 140 GeV   
base = 110 + 30* np.random.rand(4200)

# higgs signal centered at 126GeV with width of 2
gauss = 2 * np.random.randn(3000) + 126

# concatenate the signals
simpletotal = np.concatenate((base, gauss))

# plot Higgs with 15 bins
plt.figure("Total Wide Higgs Bin 2 GeV")

# extracting the number of events per bin and bin edges from the histogram data
values, binedges, junk = plt.hist(simpletotal, bins=15, range = (110, 140), alpha = 0.5, color="green")

# computing bin centers as average if its 2 bin-edges
centers = 0.5 * (binedges[1:] + binedges[:-1])

# computing expected error as the square root of values
errors = []
for each in values:
    errors.append(sqrt(each))

# plot Higgs with 15 bins
plt.hist(base, bins = 15, range = (110, 140), alpha = 0.5, color="blue")
plt.hist(gauss, bins = 15, range = (110, 140), alpha = 0.5, color="red")
plt.errorbar(centers, values, yerr = errors, ls = 'None', marker = 'x', color = 'black', markersize = 6.0 )
plt.title("Uniform Background from 4200 events; 2 Gev Higgs", backgroundcolor = "white")


plt.show()