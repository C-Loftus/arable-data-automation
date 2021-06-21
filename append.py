 # shortcut to call the converter
import csv, sys
import arableAPI,  csvOperations
import plantFormulas as pf


def appendNewRow(f, location, species):    
    if __debug__:
        print("\nENTERING READER APPEND LOOP\n")

    reader = csv.reader(f)
    foundHeaders = False
    convert = pf.data.fromValueToToIndex


    for rowList in reader:
        listToAppend = [None] * 30
        if foundHeaders == False and len(rowList) != 0:
            if rowList[0] == "local_device_time":
                foundHeaders = True
        else:
            t = 0
            for item in rowList:
                indexToValue = convert.get(t, None)
                if indexToValue != None:
                    valueToNewIndex = convert.get(indexToValue, None)
                    listToAppend[valueToNewIndex] = item
                else:
                    pass
                t += 1

        ########## calc data after putting in all given values for a row ##########
        if csvOperations.hasData(listToAppend):
            # calc date
            date = listToAppend[convert["local_device_time"]]
            if date != 0 or date != None:
                listToAppend[convert["local_device_time"]] = csvOperations.changeTimeFormat(date)

            # calc julian date
            if listToAppend[convert["local_device_time"]] != None:
                listToAppend[convert["julian_date"]] = \
                csvOperations.calcJulian(listToAppend[convert["local_device_time"]])

            # calc temperatures
            maxTInCIndex= convert["cmax_temp"]
            minTInCIndex = convert["cmin_temp"]
            for i in range(maxTInCIndex, minTInCIndex + 1 ):
                listToAppend[i] = pf.fToC(listToAppend[i + 4])

            listToAppend[convert["farm"]] = location
            listToAppend[convert["crop"]] = species
            listToAppend[convert["photosynthetic_rate"]] = \
                pf.photosyntheticRateCalc(convert["NDVI"], \
                convert["SWdw"])

            print("Outputting list :", listToAppend, "\n")
            return listToAppend

