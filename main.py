import csv, sys
from datetime import date
import arableAPI,  csvOperations
import plantFormulas as pf
import append

import drive


def main():
    print("Starting Program\n")
    try:
        toName = sys.argv[1]
        fromName = sys.argv[2]
        print("Appending to ",toName, "from ", fromName)
    except:
        print("Invalid Input. Exiting...")
    if  len(sys.argv) == 1:
        sys.exit("Error. User did not specify either of the arguments")
    if  len(sys.argv) == 2:
        sys.exit("You Didn't specify the second argument")


    # compare keys to make sure you can append correctly
    with open  (toName,  'a+', newline='',) as to:
        with open(fromName,  'r', newline='') as f:
            # get the title of the farm
            location = None
            species = None
            tempInF = True
            for line in f:
                line = line.replace(",", " ").replace("\"", " ").split(" ")
                if "Location" in line:
                    # this uses hardcoded values since arable csv output is always the same format
                    try:
                        farmInList = pf.data.farms[line[2]]
                    except KeyError:
                        print(line[2])
                        sys.exit("Farm not found in list")
                    location = line[2]
                    try: 
                        species = pf.data.speciesDict[line[3]]
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
        with open(fromName,  'r', newline='') as f:
            append.createRowToAppend(toName, f, location, species)

        # clean up at the end
        outputName = (toName).replace("csv/","")
        outputName = str(date.today()) + outputName
        csvOperations.deleteBlankRows(outputName, toName)
        drive.uploadFile(outputName)

                    


if __name__== "__main__":
    main()