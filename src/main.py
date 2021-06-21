import csv, sys
import arableAPI, plantFormulas, csvOperations


def main():
    print("Starting Program\n")
    try:
        toName = sys.argv[1]
        fromName = sys.argv[2]
        print("Appending to ",toName, "from ", fromName)
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
                    try:
                        farmInList = plantFormulas.data.farms[line[2]]
                    except KeyError:
                        print(line[2])
                        sys.exit("Farm not found in list")
                    location = line[2]
                    try: 
                        species = plantFormulas.data.speciesDict[line[3]]
                    except KeyError:
                        print(line[3])
                        sys.exit("Crop not found in list")
                      

                if "°C" in line:
                    tempInF = False
                    sys.exit("Temperature is in Celcius instead of Fahrenheit. Reconfigure the output in arable")

            print("Getting data from", location, species)

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
            


        ### append data into array ########
        with open(fromName, newline='') as f:
            if __debug__:
                print("\nENTERING READER APPEND LOOP\n")
            reader = csv.reader(f)
            foundHeaders = False
            for j in reader:
                listToAppend = [None] * 25
                if foundHeaders == False and len(j) != 0:
                    if j[0] == "local_device_time":
                        foundHeaders = True
                else:
                    t = 0
                    for item in j:
                            indexToValue = plantFormulas.data.fromFromIndexToValue.get(t, None)
                            if indexToValue != None:
                                valueToNewIndex = plantFormulas.data.fromValueToToIndex.get(indexToValue, None)
                                listToAppend[valueToNewIndex] = item
                            else:
                                pass
                            t += 1
                
                ########## clean up data after putting in all values  ##########
                    # calc julian date
                    if listToAppend[2] != None:

                        listToAppend[3] = csvOperations.calcJulian(listToAppend[2])
                    
                    maxTInCIndex= plantFormulas.data.fromValueToToIndex["cmax_temp"]
                    minTInCIndex = plantFormulas.data.fromValueToToIndex["cmin_temp"]
                    for i in range(maxTInCIndex, minTInCIndex + 1 ):
                        listToAppend[i] = plantFormulas.fToC(listToAppend[i + 4])

                    date = listToAppend[plantFormulas.data.fromValueToToIndex["local_device_time"]]
 
                    if date != 0 or date != None:
                        listToAppend[plantFormulas.data.fromValueToToIndex["local_device_time"]] = csvOperations.changeTimeFormat(date)

                    if csvOperations.hasData(listToAppend):
                        listToAppend[plantFormulas.data.fromValueToToIndex["farm"]] = location
                        listToAppend[plantFormulas.data.fromValueToToIndex["crop"]] = species

                    print("Appending list : ", listToAppend, "\n")
                            
                    csvOperations.append_list_as_row(toName, listToAppend)
        csvOperations.deleteBlankRows("newOut.csv", toName)
                    


if __name__== "__main__":
    main()
