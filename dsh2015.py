import numpy as np 
import csv
from win32api import Sleep
from csv import Dialect
import sys

csv.field_size_limit(sys.maxsize)

inputFile = 'escort_all.tsv'

outputFileStates = 'states.tsv'
outputFileCities = 'cities.tsv'

statesUSA = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District Of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states = {}
location = set()

# Function to read the data
def read_data(data):
    i = 0
    fOutputStates = csv.writer(open(outputFileStates,"r+"), dialect="excel-tab") 
    fOutputCities = csv.writer(open(outputFileCities,"r+"), dialect="excel-tab")
    fInput = csv.reader(open(inputFile,"rU"), dialect="excel-tab")
    for line in fInput:
        i = i+1
        print i
        if len(line) > 1:
            if (line[1] in statesUSA):
                if states.get(line[1]):
                    states[line[1]] = states[line[1]] + 1 
                else:
                    states[line[1]] = 1;
                fOutputStates.writerow(line)
            else:
                fOutputCities.writerow(line)
        else: 
            fOutputCities.writerow(line)
    print states         
    
def main():
    data = []
    #Read the data
    read_data(data)
  
# Standard code that calls the main() function.
if __name__ == '__main__':
  main()