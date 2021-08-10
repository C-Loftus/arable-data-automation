import sys, os
from datetime import date
import arableAPI,  csvOperations
from serialNums import private as priv
import append
import drive
import pandas as pd
import glob, os.path

# constants used for clarity
ONLY_ONE_VALID_FILE = 1
ONLY_ELEMENT = 0

# removes files intermediatary files between appending and doing
# pandas operations
def cleanUpCSVDir():
    if __debug__:
        print("Running CSV cleanup")
    filelist = glob.glob(os.path.join("csv", "*.csv"))
    for f in filelist:
        os.remove(f)

# cleans up all csv's that were downloaded from the api.
# don't need them after running the program.
def cleanUpTempDir():
    filelist = glob.glob(os.path.join("filesToReadThenDelete", "*.csv"))
    for f in filelist:
        os.remove(f)


def main():
    toName = None
    fromName = None
     # will be filled with files in ./filesToReadThenDelete by default
    fileInFromDirectory = []

    if len(sys.argv) >= 2 :
        if sys.argv[1] == "--manual":
            toName = input("Input the csv file you want to append to: ")
            fromName = input("Input the csv file you want to draw data from: ")

            fileInFromDirectory.append(fromName)
        else:
            sys.exit("You specified an argument without specifying the '--manual' flag. \
                This program automatically gets file names, so you need to specify the flag \
                to override this behavior. ")

    # we checked the manual case and it didn't run so now we can get the file names automatically
    else:
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

    ## TODO: drop duplicates could be accomplished with a more efficient
    ## way to appending. i.e. keeping a list of the last appended
    ## day and changing the API query.

    df.drop_duplicates(subset=None, inplace=True)
    outputName = toName.replace("csv/","")
    outputName = str(date.today()) + "Data Tracking Template" + ".csv"

    # Write the results to a different file
    df.to_csv(outputName, index=False)
    # upload it with the parameters specified in serialNums.py


    # hacky fix to remove blank escaped cells
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
    cleanUpTempDir()



if __name__== "__main__":
    main()
