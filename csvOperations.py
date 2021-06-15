from csv import writer, DictWriter
from enum import Enum, auto
from posixpath import join
import datetime, shutil
import pandas as pd


def createBackup(fileName):
    shutil.copy(fileName, join(fileName, datetime.date, ".backup"))


# class ColumnIndex(Enum):
#     # starts at 0 to have proper list indexing from 0
#     A  = 0
#     B  = auto()
#     C  = auto()
#     D  = auto()
#     E  = auto()
#     F  = auto()
#     G  = auto()
#     H  = auto()
#     I  = auto()
#     J  = auto()
#     K  = auto()
#     L  = auto()
#     M  = auto()
#     N  = auto()
#     O  = auto()
#     P  = auto()
#     Q  = auto()
#     R  = auto()
#     S  = auto()
#     T  = auto()
#     U  = auto()
#     V  = auto()
#     W  = auto()
#     X  = auto()
#     Y  = auto()
#     Z  = auto()

# # double enum is used so it is clear both the number and the column index
# # the usage of letters is for easy human-readability when comparing to the 
# # spreadsheet
# class ColumnName(Enum):
#     farm                    = ColumnIndex.A
#     crop                    = ColumnIndex.B
#     time                    =  ColumnIndex.C
#     julian                   = ColumnIndex.D
#     date	                  = ColumnIndex.E
#     device                 	 = ColumnIndex.F
#     T_BASE                 	 = ColumnIndex.G
#     GDD	 =                  ColumnIndex.H
#     CGDD =                  ColumnIndex.I
#     Oberserved_Growth_Stage = ColumnIndex.J
#     Estimated_Growth_Stage = ColumnIndex.K
#     cl =                   ColumnIndex.L
#     NDVI =                  ColumnIndex.M
#     ETc	 =                  ColumnIndex.N
#     SWdw	                  = ColumnIndex.O
#     maxT_C                   = ColumnIndex.P
#     meanT_C                  = ColumnIndex.Q
#     minT_C                  = ColumnIndex.R
#     precip	                = ColumnIndex.S
#     maxT_F                  = ColumnIndex.T
#     meanT_F                 = ColumnIndex.U
#     minT_F                   = ColumnIndex.V

# class headers():
    # fieldNames = [n for n in dir(ColumnName) if "__" not in n]

def calcJulian(date):
    # d = date.split("-")
    # d = list(map(int, d))
    # ts = pd.Timestamp(year = d[0], month=  d[1], day = d[2], 
    #               tz = 'US/Eastern') 
    fmt='%Y-%m-%d'
    sdtdate = datetime.datetime.strptime(date, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday
    return(jdate)


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