from csv import writer, DictWriter
import csv
from posixpath import join
import datetime, shutil


def createBackup(fileName):
    shutil.copy(fileName, join(fileName, datetime.date, ".backup"))

def deleteBlankRows(out, input):
    with open(input) as in_file:
        with open(out, 'w') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if any(field.strip() for field in row):
                    writer.writerow(row)
        

def calcJulian(date):
    try:
        fmt='%m/%d/%Y'
        sdtdate = datetime.datetime.strptime(date, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
    except:
        return None
    return(jdate)

def changeTimeFormat(date):
    try:
        s = date.split("-")
        return (s[1] + "/" + s[2] + "/" + s[0])
    except:
        return None

# the date parser for the arable format
def parseTime(date):
    try:
        t = date.replace('T', '/').split('/')
        return (t[0] + "/" + t[1] + "/" + t[3])
    except:
        return None

def hasData(input: list):
    defaultData = 2
    data = 0
    for i in input:
        if i != None:
            data+=1
    return True if data > defaultData else False


def append_list_as_row(file_name, list_of_elem):
    if list_of_elem == None or len(list_of_elem) == 0:
        return None
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def append_dict_as_row(file_name, dict_of_elem, allFieldNames):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=allFieldNames)
        # Add dictionary word to csv
        dict_writer.writerow(dict_of_elem)



# if __name__ == "__main__":
#     v = parseTime("07/24T20:00:00/2021")
#     print(v) 
#     print(calcJulian(v))