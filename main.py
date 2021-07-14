import sys, os
from datetime import date
import arableAPI,  csvOperations
from serialNums import private as priv
import append
import drive
import pandas as pd
import csv
import glob, os.path

# constants used for clarity
ONLY_ONE_VALID_FILE = 1
ONLY_ELEMENT = 0

def main():
    print("Starting Program\n")
    toName = None
    fromName = None
     # will be filled with files in ./filesToReadThenDelete by default
    fileInFromDirectory = []

    try:
        if sys.argv[1] == "--manual":
            toName = input("Input the csv file you want to append to: ")
            fromName = input("Input the csv file you want to draw data from: ")

            fileInFromDirectory.append(fromName)
        else:
            sys.exit("You specified an argument without specifying the '--manual' flag. \
                This program automatically gets file names, so you need to specify the flag \
                to override this behavior. ")

    # this exception means that len(argv) < 2 so we  know there aren't
    # any arguments passed in so we can get the file names automatically
    except IndexError:


        ## If there is only one file downloaded you know it is the only one you want to append to
        if drive.downloadFile() == ONLY_ONE_VALID_FILE:
            filesInCSVDirectory = [name for name in os.listdir('csv/')] #if os.path.isfile(name)]
            toName = "csv/" + str(filesInCSVDirectory[ONLY_ELEMENT])
        else:
        ### If you download multiple files, it is unclear which is the csv file you append to
            print("Drive downloaded multiple files that could be a possible \
                data tracking template (the file you append to). You must pick one")
            toName = input("specify the path to your file (i.e. csv/dtt.csv)")


        # gets arable api to download csv files
        arableAPI.callAPI()

        ### Creates a list with all the csv files you read from
        fileInFromDirectory = [name for name in \
             os.listdir('filesToReadThenDelete/')]

    except:
        sys.exit("Invalid Input. Exiting...")


    if __debug__:
        if len(fileInFromDirectory) < 1:
            sys.exit("No valid files to read from")


    for fromItem in fileInFromDirectory:
        fromName = "filesToReadThenDelete/" + fromItem
        print("Appending to ",toName, "from ", fromName)
        
        # compare keys to make sure you can append correctly
        with open  (toName,  'a+', newline='',) as to:
            with open(fromName,  'r', newline='') as fromCSV:
                append.appendAllValidRows(toName, fromCSV)



     # upload only final file
    # csvOperations.deleteBlankRows(toName, toName)
    df = pd.read_csv(toName, sep="\t or ,", engine='python')
    df.dropna(how='all')

    # Notes:
    # - the `subset=None` means that every column is used 
    #    to determine if two rows are different; to change that specify
    #    the columns as an array
    # - the `inplace=True` means that the data structure is changed and
    #   the duplicate rows are gone  

    ## TODO: Replace drop duplicates with a more efficient
    ## way to appending. i.e. keeping a list of the last appended
    ## day and changing the API query.

    df.drop_duplicates(subset=None, inplace=True)
    outputName = toName.replace("csv/","")
    outputName = str(date.today()) + "Data Tracking Template" + ".csv"

    # Write the results to a different file
    df.to_csv(outputName, index=False)
    # upload it with the parameters specified in serialNums.py


    # hacky fix
    # explanation:
    # pandas adds a \" char at the start of lines with blank cells 
    # for some reason. I need to remove the quotes otherwise the 
    # spreadsheet parser will think each row is just one big cell
    with open(outputName, 'r') as infile:
        with open("Data Tracking Template", 'w') as outfile:
            data = infile.read()
            data = data.replace('"', "")
            outfile.write(data)

    drive.uploadFile("Data Tracking Template")

    cleanUpCSVDir()
    # cleanUpTempDir()



if __name__== "__main__":
    main()




def cleanUpCSVDir():
    filelist = glob.glob(os.path.join("csv", "*.csv"))
    for f in filelist:
        os.remove(f)

def cleanUpTempDir():
    filelist = glob.glob(os.path.join("filesToReadThenDelete", "*.csv"))
    for f in filelist:
        os.remove(f)





            # with open(fromName,  'r', newline='') as f:
            #     # get the title of the farm
            #     location = None
            #     species = None
            #     for line in f:
            #         line = line.replace(",", " ").replace("\"", " ").split(" ")
            #         if "Location" in line:
            #             # this uses hardcoded values since arable 
            #             # csv output is always the same format

            #             # check to make sure you are taking data
            #             # from a valid farm/crop
            #             try:
            #                 farmInList = priv.farms[line[2]]
            #             except KeyError:
            #                 print(line[2])
            #                 sys.exit("Farm not found in list")
            #             location = line[2]
            #             try: 
            #                 species = priv.speciesDict[line[3]]
            #             except KeyError:
            #                 print(line[3])
            #                 sys.exit("Crop not found in list")

            #         if "°C" in line:
            #             sys.exit("Temperature is in Celcius instead of Fahrenheit. \
            #                 Reconfigure the output in arable")

            #     print("Getting data from", location, species)

            ### append data into array after assuring valid data ########
