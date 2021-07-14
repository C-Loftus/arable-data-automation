import csv
import arableAPI,  csvOperations
from serialNums import private as priv
import plantFormulas

ARABLE_DEFAULT_HEADER = "local_device_time"

def appendAllValidRows(toName, f):    
    if __debug__:
        print("\nENTERING READER APPEND LOOP\n")

    reader = csv.reader(f)
    print("Reading from", f)

    # don't want to append the first row since those are just the column names
    reader.__next__()

    for rowList in reader:
        listToAppend = [None] * 30
        indexOfItem = 0
        for item in rowList:
            # converts from old index to the val assoc. with it
            indexToValue = priv.fromFromIndexToValueNEW.get(indexOfItem, None)
            # if a valid val was found, do the conversion to get the index in the output csv file
            if indexToValue != None:
                valueToNewIndex = priv.fromValueToToIndex.get(indexToValue, None)
                listToAppend[valueToNewIndex] = item
            else:
                if __debug__:
                    print("Item:", item, "can't be converted at the unused index:", indexOfItem)
            indexOfItem += 1
        ###### calc data after putting in all given values for a row ##########
        calculateDataPoints(listToAppend)

        print("\nAppending : ", listToAppend)
        csvOperations.append_list_as_row(toName, listToAppend)


# all strings in this func are column headers for things that need to be calculated. 
# They aren't output by default in the arable sensor
def calculateDataPoints(listToAppend):
    if csvOperations.hasData(listToAppend):
        convert = priv.fromValueToToIndex


        sensorID = listToAppend[convert["device"]]
        # expand to full name 
        species = priv.sensorLocations[sensorID].split(" ")[1]

        location = priv.sensorLocations[sensorID].split(" ")[0]


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