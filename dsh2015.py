import numpy as np 
import csv
from win32api import Sleep
from csv import Dialect
import sys
import extractPrice
import outputStats

csv.field_size_limit(sys.maxsize)
inputFile = 'escort_states.tsv'
#outputFile = 'escort_states.csv'

stateData = {}
yearStats = {}

def processRow(line,lineSize):
    if stateData.has_key(line[1]):
        yearStats =  stateData[line[1]]
    else:
        yearStats = {}
    date = "NA"
    if lineSize > 6:
        date = line[6][:4]
    price = extractPrice.get_prices(line[3])
    if(yearStats.has_key(date)):
        if price != 0:
            priceList = yearStats[date]         
            priceList.append(price)
            yearStats[date] = priceList
    else:
        priceList = []
        if price!=0: 
            priceList.append(price)
        yearStats[date] = priceList
    stateData[line[1]] = yearStats  

# Function to read the data
def read_data(data):
    #fOutput = csv.writer(open(outputFile,"wb"), dialect="excel-tab")
    fInput = csv.reader(open(inputFile,"rU"), dialect="excel-tab")
    i = 0
    for line in fInput:
        lineSize =  len(line)
        if lineSize > 1:
            i = i + 1
            print i
            processRow(line,lineSize)
    outputStats.printStats(stateData)
        
def main():
    data = []
    #Read the data
    read_data(data)
  
# Standard code that calls the main() function.
if __name__ == '__main__':
    main()