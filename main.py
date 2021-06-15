import csv
from os import name
import arableAPI, plantFormulas, csvOperations
from csv import writer
from collections import defaultdict

def main():
    print("Starting Program\n")
    try:
        csvName = input("Enter the name of the CSV file you will be expanding : ")
        fromName = input("Enter the name of the CSV file from which you will draw the data : ")
        
    except:
        print("Invalid Input. Exiting...")
        exit

    # compare keys to make sure you can append correctly
    with open(csvName) as to:

        lis = [line.split() for line in to]        # create a list of lists
        for i in range(len(lis)):   
            if len(lis[i]) > 5:
                toListCols = lis[i]
                break

    with open(fromName) as f:

        lis = [line.split() for line in f]        # create a list of lists
        for i in range(len(lis)):    
            if len(lis[i]) > 5:
                fromListCols = lis[i]
                break

    with open(csvName) as to:
        with open(fromName) as f:
            indexOfSharedItemsInFrom = {}
            indexOfSharedItemsInTo = {}
            both = []

# unfortunately no better way than O(N^2) since we don't know any info about the cols before passing them in
            for fromIndex, fromValue in enumerate(toListCols):
                for toIndex, toValue in enumerate(fromListCols):
                    if toValue == fromValue:
                        both.append(toValue)
                        indexOfSharedItemsInFrom[fromIndex] = fromValue
                        indexOfSharedItemsInTo[toIndex] = toValue

            dictionaryToInsert = dict.fromkeys(both)
            gotColumnNames = False

            lis = [line.split() for line in f]        # create a list of lists
            for i in range(len(lis)):
                if gotColumnNames == False:
                    if both in lis[i]:
                        gotColumnNames = True
                else:
                    # unsure on +1
                    for i in range(len(lis[i] + 1)):
                        if i in indexOfSharedItemsInFrom:
                            columnName = indexOfSharedItemsInFrom[i]
                            dictionaryToInsert[columnName] = lis[i]
                    
                    print("Added ", dictionaryToInsert)
                    csvOperations.append_dict_as_row(csvName, toListCols, dictionaryToInsert)

        
        
 

if __name__== "__main__":
    main()
