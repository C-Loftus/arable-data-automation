import csv
import arableAPI, plantFormulas, csvOperations
from csv import writer


def main():
    print("Starting Program\n")
    try:
        csvName = input("Enter the name of the CSV file you will be expanding:")
        fromName = input("Enter the name of the CSV file from which you will draw the data")
        
    except:
        print("Invalid Input. Exiting...")
        exit

    # compare keys to make sure you can append correctly
    with open(csvName) as to:
        toList = []

        lis = [line.split() for line in to]        # create a list of lists
        for i in lis:   
            if len(list) > 5:
                toListCols = lis[i]
                break

    with open(fromName) as from:
        fromList = []

        lis = [line.split() for line in from]        # create a list of lists
        for i in lis:    
            if len(list) > 5:
                fromListCols = lis[i]
                break

    
    
    # for i in toList:
    #     if toList[i] != fromList[i]:
    #         print("Your csv files do not match up. You cannot append to ", csvName, "from ", fromName)


    with open(csvName) as f:
        dictionaryToInsert = dict.fromkeys(toList)

        gotColumnNames = False
        lis = [line.split() for line in f]        # create a list of lists
        for i in lis:    
            if lis[i] == toList and gotColumnNames == False:
                gotColumnNames = True
            else:
                data = lis[i]
                csvOperations.append_dict_as_row

        
        


if __name__ == "main":
    main()
