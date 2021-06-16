import csv, sys
from shutil import Error
from os import name
from typing import Collection
import arableAPI, plantFormulas, csvOperations
from csv import writer
from collections import defaultdict


def main():

    farms = {
                "CG" : "Cherry Grove",
                "AA": " Abe's Acres",
                "OO": "Orchard Organics", 
                "BRF": "Big Red Farm",
                "TS" : "Isles"
        }

        # alternative spellings included just in case the users inputs data wrong
    speciesDict = {
        "ChTom" : "cherry tomato",
        "CherryTom": "cherry tomato",
        "StTom" : "standard tomato",
        "StdTom" : "standard tomato",
        "chard" : "chard",
        "chrd" : "chard", 
        "Chard" : "chard", 
        "Zuke" : "zucchini",
        "zucke" : "zucchini",
        "zuc" : "zucchini",
    }
    print("Starting Program\n")
    try:
        #   toName = input("Enter the name of the CSV file you will be expanding : ")
        # fromName = input("Enter the name of the CSV file from which you will draw the data : ")
        toName = sys.argv[1]
        print("Appending to ",toName)
        fromName = sys.argv[2]
        print("from ", fromName)
        
    except:
        print("Invalid Input. Exiting...")
        exit

    # compare keys to make sure you can append correctly
    with open  (toName, newline='') as to:
        with open(fromName, newline='') as f:

            # get the title of the farm
            location = None
            species = None
            tempInF = True
            for line in f:
                line = line.replace(",", " ").replace("\"", " ").split(" ")
                
                # line = d.strip(" ") # separate species and location
                # print(line, type(line))
                if "Location" in line:
                    print(line)
                    try:
                        farmInList = farms[line[2]]
                    except KeyError:
                        print(line[2])
                        sys.exit("Farm not found in list")
                    location = line[2]
                    try: 
                        species = speciesDict[line[3]]
                    except KeyError:
                        print(line[3])
                        sys.exit("Crop not found in list")
                      

                if "°C" in line:
                    tempInF = False
                    sys.exit("Temperature is in Celcius instead of Fahrenheit. Reconfigure the output in arable")



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

            # if __debug__:
            #     print("from", fromListCols)

            
            fromValueToToIndex = defaultdict(lambda a: None)
            fromValueToToIndex    = {
                "farm" : 0,
                "crop" : 1,
                "local_device_time" : 2, 
                # "julian date" : 3,
                "device" : 4, 
                "cl" : 10,
                "NDVI" : 11,
                "ETc" :12,
                "SWdw": 13,
                "cmax_temp": 14,  # celcius
                "cmean_temp": 15, # celcius
                "cmin_temp": 16, # celcius
                "precip": 17,
                "max_temp": 18,  # f
                "mean_temp": 19, # f
                "min_temp": 20, # f,
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
                19:  "min_temp",
                20:  None,
                21:  None,  
                22: None,
                23 : "precip",
            }

            both = ["local_device_time", "device", "cl", "NDVI", "ETc", "SWdw", "max_temp", "mean_temp",	"min_temp", "precip"]
            
            if __debug__:
                print("\nENTERING READER APPEND LOOP\n")

                ### append data into array ########
        with open(fromName, newline='') as f:
            reader = csv.reader(f)
            for j in reader:
                print("1")
                t = 0
                listToAppend = [None] * 25
                for item in j:
                    indexToValue = fromFromIndexToValue.get(t, None)
                    if indexToValue != None:
                        valueToNewIndex = fromValueToToIndex.get(indexToValue, None)
                        listToAppend[valueToNewIndex] = item
                    else:
                        pass
                    t += 1
                print("Appending row ", j)

                if __debug__:
                    j = 0
                    for i in listToAppend:
                        print(j, i)
                        j+=1

                ########## clean up data ##########

                # calc julian date
                if listToAppend[2] != None:
                    if __debug__:
                        print("Julian date = ", csvOperations.calcJulian(listToAppend[2]))
                    listToAppend[3] = csvOperations.calcJulian(listToAppend[2])
                
                # calc celcius temps from f
                maxTInCIndex= fromValueToToIndex["cmax_temp"]
                minTInCIndex = fromValueToToIndex["cmin_temp"]
                for i in range(maxTInCIndex, minTInCIndex + 1 ):
                    # print(i, listToAppend[i])
                    # if listToAppend[i] != None:
                        # if __debug__:
                        #     print("F value", plantFormulas.fToC(listToAppend[i]))
                    listToAppend[i] = plantFormulas.fToC(listToAppend[i + 4])

                # if __debug__:
                #     print(listToAppend)
                #     if listToAppend[20] != None and listToAppend[17] == None:
                #         if listToAppend[17] != '':
                #             sys.exit("error invalid temp C")

                date = listToAppend[fromValueToToIndex["local_device_time"]]
                if date != 0 or date != None:
                    listToAppend[fromValueToToIndex["local_device_time"]] = csvOperations.changeTimeFormat(date)

                listToAppend[fromValueToToIndex["farm"]] = location
                listToAppend[fromValueToToIndex["crop"]] = species

                print("Appending list : ", listToAppend, "\n")
                        
                csvOperations.append_list_as_row(toName, listToAppend)
                                

if __name__== "__main__":
    main()
