import numpy as np
import matplotlib.pyplot as plt

# Background
###############################
plt.show()

# random array with 42000 elements according to the uniform distribution
testrand = np.random.rand(42000)  

# generating a uniform background(base) between a 110 GeV and 140 GeV                 
base = 110 + 30* np.random.rand(42000)    

# boolean index which has True for samples greater than testrand; 
# this percentage reduces linearly as the value for background increases  
index = (1.0 - 0.5 * (base - 110)/ 30) > testrand      

# take a subset of the index to create a sloping background
sloping = base[index] 

# plot Sloping background
plt.figure("Sloping")
plt.hist(sloping, bins = 15, range = (110, 140))
plt.title("Sloping Background from 42000 events", backgroundcolor = "white")

# Gaussian Higgs signal
###############################
# signal centered at 126GeV with width of 2
gauss = 2 * np.random.randn(300) + 126

# signal centerd at 126GeV with width of 0.5
narrowGauss = 0.5 * np.random.randn(300) + 126

# plot Higgs
plt.figure("HiggsAlone")
plt.hist(gauss, bins = 15, range = (110,140))
plt.title("2Gev Higgs in 2 GeV bins on its own", backgroundcolor = "white")

# Higgs signal + Gaussian signal
###############################

# concatenate the signals
total = np.concatenate((sloping, gauss))   
narrowTotal = np.concatenate((sloping, narrowGauss)) 

# plot the 3 kinds of signals with 30 bins each
plt.figure("Total Narrow Higgs Bin 1 GeV")
plt.hist(narrowTotal, bins = 30, range = (110,140), alpha = 0.5) 
plt.hist(sloping, bins = 30, range = (110,140), alpha = 0.5) 
plt.hist(narrowGauss, bins = 30, range = (110,140), alpha = 0.5) 
plt.title("0.5 Gev Higgs in 1 GeV bins with Sloping Background", backgroundcolor = "white")
plt.show()


# Higgs signal with 3000 signals
###############################
# signal centered at 126GeV with width of 2
gaussbig = 2 * np.random.randn(30000) + 126 

# signal centerd at 126GeV with width of 0.5                 
gaussnarrowbig = 0.5 * np.random.randn(30000) + 126

# concatenate the signals
totalbig = np.concatenate((sloping, gaussbig))

# plot the 3 kinds of signals with 60 bins each
plt.figure("30000 Higgs in 0.5 GeV bins")
plt.hist(gaussnarrowbig, bins=60, range =(110,140), alpha = 0.5) #Higgs signal 
plt.hist(gaussbig, bins = 60, range =(110,140), alpha = 0.5)
plt.title("30000 Narrow and Wide Higgs in 0.5 GeV bins", backgroundcolor = "white")


# Higgs signal + Gaussian signal with errors
###############################
plt.figure("Total Wide Higgs Bin 2 GeV with errors")

# extracting values and bin edges from the histogram data
values, binedges, junk = plt.hist(total, bins = 15, range = (110, 140), alpha = 0.5, color = "blue")  

# computing bin centers as average if its 2 bin-edges
centers = 0.5 * (binedges[1:] + binedges[:-1])  

# computing expected error as the square root of values
errors = np.sqrt(values)   

plt.hist(total, bins = 15, range = (110, 140), alpha = 0.5, color = "blue")                                
plt.hist(sloping, bins = 15, range = (110, 140), alpha = 0.5, color = "green")                              
plt.hist(gauss, bins = 15, range = (110, 140), alpha = 0.5, color = "red")                                  
plt.errorbar(centers, values, yerr = errors, ls = 'None', marker ='x', color = 'black', markersize = 6.0 ) 
plt.title("2 Gev Higgs in 2 GeV bins with Sloping Background + Errors", backgroundcolor = "white")



plt.show()




# change Base to lowercase
