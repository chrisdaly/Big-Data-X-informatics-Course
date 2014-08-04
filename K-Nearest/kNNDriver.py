import kNN                                                             #importing the methods and variables from kNN.py. these methods/variables can be accessed as kNN.MethodName() or kNN.variableName
import matplotlib.pyplot as plt
import numpy as np

# Plotting a basic data set and testing classification
###############################

# create a plot
FigDating = plt.figure()

# create the dataset with four items(2-D vectors) each one associated with a label
group, labels = kNN.createDataSet() 

# color map                                    
colormap1 = { 'A':'red', 'B':'blue'} 

# array for storing the labels                                   
ColoredGroupLabels = []

# extract the corresponding colour to each value in the dataset
for label in labels:                                                  
    ColoredGroupLabels.append(colormap1[label])                       

# divide the figure into 3 sub plots (3 rows 1 column 1st plot), specifying the axes limits
ax1 = FigDating.add_subplot(311, xlim = (-0.1, 1.1), ylim = (-.05, 1.15))    

# plot the data as a scatter plot with color(c) property as per the labelling. 
ax1.scatter(group[:,0], group[:,1], s = 20, c = ColoredGroupLabels, marker = 'o' )   

# testing with new points
# first point - created, classified and plotted
testvector = [.2, .2]
answer1 = kNN.classify0(testvector, group, labels, 3)                     
ax1.scatter(testvector[0], testvector[1], s= 20, c = colormap1[answer1], marker = 'x' )

#second point - created, classified and plotted
testvector = [.5, .5]                                                   
answer2 = kNN.classify0(testvector,group, labels, 3)
ax1.scatter(testvector[0], testvector[1], s= 20, c = colormap1[answer2], marker = 'x' )
 
#third point - created, classified and plotted
testvector = [.75, .75]
answer3 = kNN.classify0(testvector,group, labels, 3)
ax1.scatter(testvector[0], testvector[1], s= 20, c = colormap1[answer3], marker = 'x' )


# Perform K-Nearest Neighbor classification on the datingTestSet2 data set
###############################

# load dataset from file
datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')  

# create an array for the labels
datingLabelArray = np.array(datingLabels)                                                   

# color map
colormap2 = { 1:'red', 2:'blue', 3:'green' }

# array for storing the labels 
ColoredDatingLabel = [] 

# extract the corresponding colour to each value in the dataset
for label in datingLabelArray:
    ColoredDatingLabel.append(colormap2[label])

# 2nd subplot, specifying the axes limits
ax2 = FigDating.add_subplot(312, xlim = (0, 100000), ylim = (0, 25))    

# plot the data as a scatter plot with color(c) property as per the labelling.                                  
ax2.scatter(datingDataMat[:,0], datingDataMat[:,1], s= 20, c= ColoredDatingLabel, marker = 'o' )  

# normalize the dataset for 3rd subplot
normMat, ranges, minVals = kNN.autoNorm(datingDataMat)    

# 3rd subplot, specifying the axes limits
ax3 = FigDating.add_subplot(313, xlim=(0, 1), ylim=(0, 1))   

# plot the normalized data as a scatter plot with color(c) property as per the labelling.  
ax3.scatter(normMat[:,0], normMat[:,1], s = 20, c= ColoredDatingLabel, marker = 'o' )

plt.show()

totalErorr = kNN.datingClassTest(0.1) 












# lowercase ColoredGroupLabels

