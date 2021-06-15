import csv, sys
from os import name
from typing import Collection
import arableAPI, plantFormulas, csvOperations
from csv import writer
from collections import defaultdict

def main():
    print("Starting Program\n")
    try:
        #   toName = input("Enter the name of the CSV file you will be expanding : ")
        # fromName = input("Enter the name of the CSV file from which you will draw the data : ")
        toName = sys.argv[1]
        fromName = sys.argv[2]
        
    except:
        print("Invalid Input. Exiting...")
        exit

    # compare keys to make sure you can append correctly
    with open  (toName, newline='') as to:
        with open(fromName, newline='') as f:
            toListCols = []
            reader = csv.reader(to)
            for row in reader:   
                if len(row) > 20:
                    toListCols = row
                    break

            reader = csv.reader(f)
            for row in reader:   
                if "local_device_time" in row:
                    fromListCols = row
                    break

            if __debug__:
                print("from", fromListCols)

            
            fromValueToToIndex = defaultdict(lambda a: None)
            fromValueToToIndex    = {
                "farm" : 0,
                # "crop" : 1
                "local_device_time" : 2, 
                # "julian date" : 3,
                "device" : 4, 
                "cl" : 10,
                "NDVI" : 11,
                "ETc" :12,
                "SWdw": 13,
                "max_temp": 14,
                "mean_temp": 15,
                "min_temp": 16,
                "precip": 17,
                }


            fromFromIndexToValue = defaultdict(lambda a: None)
            fromFromIndexToValue = {
                0: "local_device_time",
                1: "device",
                2: None  ,
                3: None  ,
                4: None  ,
                5: "cl",
                6:  None ,
                7: "ETc"  ,
                8:  None ,
                9:  None ,
                10:  None ,
                11:  None ,
                12:  "NDVI" ,
                13:  None,
                14 : None  ,
                15:  None ,
                16:  "SWdw" ,
                17:  "max_temp",      
                18:  "mean_temp" ,
                19:   "min_temp",
                20:  None,
                21:  None,  
                22: None,
                23 : "precip",
            }

            both = ["local_device_time", "device", "cl", "NDVI", "ETc", "SWdw", "max_temp", "mean_temp",	"min_temp", "precip"]
            
            if __debug__:
                print("\nENTERING READER APPEND LOOP\n")
            reader = csv.reader(f)
            for row in reader:
                print("\nRow in ", fromName, " : ", row)
                t = 0
                listToAppend = [None] * len(toListCols)
                for item in row:
                    indexToValue = fromFromIndexToValue.get(t, None)
                    if indexToValue != None:
                        valueToNewIndex = fromValueToToIndex.get(indexToValue, None)
                        listToAppend[valueToNewIndex] = item
                    else:
                        pass

                    t += 1
                print("Appending")
                # calc julian date
                if listToAppend[2] != None:
                    listToAppend[3] = csvOperations.calcJulian(listToAppend[2])
                csvOperations.append_list_as_row(toName, listToAppend)
                                

if __name__== "__main__":
    main()
