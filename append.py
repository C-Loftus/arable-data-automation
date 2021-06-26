import csv
import arableAPI,  csvOperations
from serialNums import private as priv
import plantFormulas

ARABLE_DEFAULT_HEADER = "local_device_time"

def appendAllValidRows(toName, f, location, species):    
    if __debug__:
        print("\nENTERING READER APPEND LOOP\n")

    reader = csv.reader(f)
    foundHeaders = False


    for rowList in reader:
        listToAppend = [None] * 30
        if foundHeaders == False and len(rowList) != 0:
            if rowList[0] == ARABLE_DEFAULT_HEADER:
                foundHeaders = True
        else:
            indexOfItem = 0
            for item in rowList:
                # converts from old index to the val assoc. with it
                indexToValue = priv.fromFromIndexToValue.get(indexOfItem, None)
                # if a valid val was found, do the conversion to get the index in the output csv file
                if indexToValue != None:
                    valueToNewIndex = priv.fromValueToToIndex.get(indexToValue, None)
                    listToAppend[valueToNewIndex] = item
                else:
                    if __debug__:
                        print("Item:", item, "can't be converted at the unused index:", indexOfItem)
                indexOfItem += 1

            ###### calc data after putting in all given values for a row ##########
            calculateDataPoints(listToAppend, location, species)
            if __debug__:
                print("Appending : ", listToAppend)
            csvOperations.append_list_as_row(toName, listToAppend)


# all strings in this func are column headers for things that need to be calculated. 
# They aren't output by default in the arable sensor
def calculateDataPoints(listToAppend, location, species):
    if csvOperations.hasData(listToAppend):
        convert = priv.fromValueToToIndex

        # calc date
        date = listToAppend[convert["local_device_time"]]
        if date != 0 or date != None:
            listToAppend[convert["local_device_time"]] = csvOperations.changeTimeFormat(date)
        # calc julian date
        if listToAppend[convert["local_device_time"]] != None:
            listToAppend[convert["julian_date"]] = csvOperations.calcJulian(listToAppend[convert["local_device_time"]])
        # calc temperatures
        maxTInCIndex= convert["cmax_temp"]
        minTInCIndex = convert["cmin_temp"]
        for i in range(maxTInCIndex, minTInCIndex + 1 ):
            listToAppend[i] = plantFormulas.fToC(listToAppend[i + 4])

        listToAppend[convert["farm"]] = location
        listToAppend[convert["growing_environment"]] = plantFormulas.environment(listToAppend[convert["device"]])
        listToAppend[convert["crop"]] = species
        listToAppend[convert["photosynthetic_rate"]] = \
            plantFormulas.photosyntheticRateCalc((listToAppend[convert["NDVI"]]), \
            (listToAppend[convert["SWdw"]]))

        listToAppend[convert["T_base"]] = priv.TBase[species]
    else:
        # don't do anything on an empty row
        if __debug__:
            print("Empty row, not calc'ing anything")
    return