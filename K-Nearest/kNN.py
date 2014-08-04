from numpy import *
import operator
from os import listdir

# Sets up a datset of 4 (2D vector) items -- each of which has one of two labels
###############################
def createDataSet():

    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']

    return group, labels


# Uses k Nearest Neighbors to classify inX according to existing dataSet with known ratings in labels
###############################
def classify0(inX, dataSet, labels, k):

	# number of rows in dataSet
	dataSetSize = dataSet.shape[0]	

	# array of same shape as dataSet holding inX-dataSet entry in each position
	diffMat = tile(inX, (dataSetSize,1)) 

	# subtract the original dataSet
	diffMat = diffMat - dataSet

	# square entries in diffMat
	sqDiffMat = diffMat**2

	# sum over vector components
	sqDistances = sqDiffMat.sum(axis = 1)

	# traditional Euclidean distance for each dataSet entry
	distances = sqDistances**0.5	

	# argsort returns indices that sort distances   
	sortedDistIndicies = distances.argsort()

	# an empty dictionary key:value pairs
	# key = labels  value = number times this label in set of k
	classCount = {}

	# loop through k nearest neighbors
	for i in range(k):	

		# label of this neighbor
        voteIlabel = labels[sortedDistIndicies[i]]	

        # get gets current count for voteIlabel and returns zero if first time voteIlabel seen (default = 0)
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1	

    # sort classCount (highest to lowest) by voteIlabel count
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)	
    
    # the label that occurs most often in k nearest neighbors
    return sortedClassCount[0][0]	


# Reads rating data and returns a matrix of 1000 rows of 3 Vectors, and an array of numeric labels
###############################
def file2matrix(filename):

    fr = open(filename)

    # get the number of lines in the file
    numberOfLines = len(fr.readlines())   

    # prepare matrix to return  
    returnMat = zeros((numberOfLines,3))   

    # prepare labels return       
    classLabelVector = []  

    fr = open(filename)

    # index for rows
    index = 0

    # go through each line of the file
    for line in fr.readlines():

    	# strip white space and split at tabs
        line = line.strip()
        listFromLine = line.split('\t')

        # store the 3 pieces of data in the returnMat matrx
        returnMat[index,:] = listFromLine[0:3]

        # store the label data in the classLabelVector array
        classLabelVector.append(int(listFromLine[-1]))

        index += 1

    return returnMat,classLabelVector


# Normalizes vector components to be between 0 and 1 
###############################
def autoNorm(dataSet):

	# get the minimum and maximum rows in the dataset
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)

    # compute the range array
    ranges = maxVals - minVals

    # create an array with the same dimensions and fill it with zeros
    normDataSet = zeros(shape(dataSet))

    # get the number of rows of the dataset
    m = dataSet.shape[0]

    # create a matrix full of the minimum values and subtract it from the dataSet
    normDataSet = dataSet - tile(minVals, (m,1))

    # divide the new matrix element wise by a matrix full of the range array
    normDataSet = normDataSet / tile(ranges, (m,1)) 

    return normDataSet, ranges, minVals


# Uses 90% data to predict the other 10% (hoRatio = hold out percentage). Prints fraction of errors
###############################
def datingClassTest(hoRatio):

	# load dataset from file
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')       

    # normalize the dataset
    normMat, ranges, minVals = autoNorm(datingDataMat)

    # get the number of rows of the dataset
    m = normMat.shape[0]

    # multiply the hold out ratio by the number of rows and convert to integer
    numTestVecs = int(m * hoRatio)

    # counter for errors
    errorCount = 0.0

    # loop through the test vectors
    for i in range(numTestVecs):

    	# use the classify function to predict the class
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:], 
        							datingLabels[numTestVecs:m], 3)

        # if the prediction isn't equal to the actual classification then increment the errorCount
        if (classifierResult != datingLabels[i]): 
        	errorCount += 1.0

    # print out the results
    print "The total error rate is: %f" % (errorCount/float(numTestVecs))
    print "The total number of errors is %f" % errorCount


# Addition to generate file for 3D PLotting system PlotViz
###############################
def WritePlotViz(filename):

	# open/create a PlotViz file in write mode
	PVFile = open(filename, 'w')

	# load dataset from file
	datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')

	# normalize the dataset
	normMat, ranges, minVals = kNN.autoNorm(datingDataMat)

	# loop through the normalized matrix
	for i in range(normMat.shape[0]):

		# write the information with each entry separated via a tab
		PVFile.write( "%d\t%f\t%f\t%f\t%d\n" %(i, normMat[i,0], normMat[i,1], 
												normMat[i,2], datingLabels[i]))

