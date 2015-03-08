import csv
import numpy as np

outputFile = 'states_stats.csv'

def printStats(stateDate):
    fOutput = csv.writer(open(outputFile,"wb"))
    for key1, value1 in stateDate.iteritems():
        for key,value in value1.iteritems():
            line = []
            line.append(key1)
            line.append(key)
            if len(value) != 0:
                line.append(np.mean(value))
                line.append(np.median(value))
                line.append(np.min(value))
                line.append(np.max(value))
                line.append(len(value))
            else: 
                line.append("NA")
                line.append("NA")
                line.append("NA")
                line.append("NA")
                line.append("NA")
            fOutput.writerow(line)
    print "Output Done"
    