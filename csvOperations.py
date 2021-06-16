from csv import writer, DictWriter
from enum import Enum, auto
from posixpath import join
import datetime, shutil


def createBackup(fileName):
    shutil.copy(fileName, join(fileName, datetime.date, ".backup"))


def calcJulian(date):
    try:
        fmt='%Y-%m-%d'
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

def hasData(input: list):
    return


def append_list_as_row(file_name, list_of_elem):
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