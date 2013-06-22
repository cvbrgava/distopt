#!/usr/bin/python
# -*- coding: utf-8 -*-
def dynamicprog( weights , values, volume ):
	for index in range( len( weights ) ) :
		if index == 0 :
			old = [ (0,[0]) if weights[index] > vol else (values[index], [1]) for vol in range( volume + 1 )]                	
		else :			
        		old = [ (old[vol][0], old[vol][1]+[0])  for vol in range( volume + 1 ) if vol < weights[ index ]]+[ (old[vol][0], old[vol][1]+ [0]) if (old[vol][0]) > (values[ index ] + old[vol - weights[ index ] ][0])  else (values[ index ] + old[vol - weights[ index ] ][0], old[vol - weights[ index ] ][1]+[1])  for vol in range( volume + 1 ) if vol >= weights[ index ] ]
        return old[ -1 ][ 0 ] , old[ -1 ] [ 1 ] 


def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    
    value, taken  = dynamicprog( weights , values, capacity )

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

