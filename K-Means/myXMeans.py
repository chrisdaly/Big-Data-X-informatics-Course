from pylab import plot,show
from numpy import array
from scipy.cluster.vq import kmeans,vq
import numpy as np
import matplotlib.pyplot as plt


# Loads a CSV file into an array, converts elements to strings, returns a list of tuples
###############################
def loadCSV(fileName):

    # open the file and read the content
    fileHandler = open(fileName, "rt")
    lines = fileHandler.readlines()
    fileHandler.close()

    # remove the header
    del lines[0] 


    dataset = []
    for line in lines:
        instance = lineToTuple(line)
        instance = np.delete(instance,0,0)
        dataset.append(instance)


    return array(dataset, dtype = np.float32)


# Converts a comma separated string into a tuple
###############################
def lineToTuple(line):

    # remove leading/trailing whitespace and newlines
    cleanLine = line.strip()      

    # remove quotes          
    cleanLine = cleanLine.replace('"', '')

    # separate the fields via commas
    lineList = cleanLine.split(",")

    # convert strings into number         
    stringsToNumbers(lineList)

    # conver to an array
    lineTuple = array(lineList)

    return lineTuple


# Destructively converts all the string elements represting numbers to floats
###############################
def stringsToNumbers(myList):

    for i in range(len(myList)):
        # checks if the string can be safely converted to a float
        if (isValidNumberString(myList[i])):
            myList[i] = float(myList[i])


# Checks if a given string can be safely converted into a positive float
###############################
def isValidNumberString(s):

  if len(s) == 0:
    return False

  # ignore dashes
  if len(s) > 1 and s[0] == "-":
    s = s[1:]

  for c in s:
    # if the character is not a number then return False
    if c not in "0123456789.":
      return False
      
  return True

# data generation. Set file location here
data = loadCSV("data.csv")

# computing K-Means with K = 2 (2 clusters)but you can change this. Plot works upto 5 clusters
K=3
centroids,_ = kmeans(data,K)
# assign each sample to a cluster
idx,_ = vq(data,centroids)

# some plotting using numpy's logical indexing
plt.figure("Clustering K={0} Life Expectancy vs GDP per country".format(K))
#plt.semilogy
plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or', data[idx==2,0],
     data[idx==2,1],'og', data[idx==3,0],data[idx==3,1],'oy', data[idx==4,0],data[idx==4,1],'om')
plot(centroids[:,0],centroids[:,1],'sk',markersize=3)
plt.xlabel("Life Expectancy")
plt.ylabel("GDP (nominal)")
plt.title("Graph of Life Expectancy vs GDP per country")
show()