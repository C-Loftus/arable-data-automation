
from typing import List
from collections import defaultdict


class data:
    farms = {
                "CG" : "Cherry Grove",
                "AA": " Abe's Acres",
                "OO": "Orchard Organics", 
                "BRF": "Big Red Farm",
                "TS" : "Isles"
        }

        # alternative spellings included just in case the users inputs data wrong
    speciesDict = {
        "ChTom" : "cherry tomato",
        "CherryTom": "cherry tomato",
        "StTom" : "standard tomato",
        "StdTom" : "standard tomato",
        "chard" : "chard",
        "chrd" : "chard", 
        "Chard" : "chard", 
        "Zuke" : "zucchini",
        "zucke" : "zucchini",
        "zuc" : "zucchini",
    }
    fromValueToToIndex = defaultdict(lambda a: None)
    fromValueToToIndex    = {
                "farm" : 0,
                "crop" : 1,
                "local_device_time" : 2, 
                # "julian date" : 3,
                "device" : 4, 
                "cl" : 10,
                "NDVI" : 11,
                "ETc" :12,
                "SWdw": 13,
                "cmax_temp": 14,  # celcius
                "cmean_temp": 15, # celcius
                "cmin_temp": 16, # celcius
                "precip": 17,
                "max_temp": 18,  # f
                "mean_temp": 19, # f
                "min_temp": 20, # f,
                }                


    fromFromIndexToValue = defaultdict(lambda a: None)
    fromFromIndexToValue = {
                0: "local_device_time",
                1: "device",
                2: None  ,
                3: None  ,
                4: None  ,
                5: "cl",
                6:  None ,
                7: "ETc"  ,
                8:  None ,
                9:  None ,
                10:  None ,
                11:  None ,
                12:  "NDVI" ,
                13:  None,
                14 : None  ,
                15:  None ,
                16:  "SWdw" ,
                17:  "max_temp",      
                18:  "mean_temp" ,
                19:  "min_temp",
                20:  None,
                21:  None,  
                22: None,
                23 : "precip",
            }

    both = ["local_device_time", "device", "cl", "NDVI", "ETc", "SWdw", "max_temp", "mean_temp", "min_temp", "precip"]


def celciusToF(tempInC):
    try:
        tempInC = float(tempInC)
    except:
        return None
    return format(((9 * float(tempInC)) / 5)+32, '.1f')

def fToC(tempInF):
    try:
        tempInF = float(tempInF)
    except:
        return None
    return format(((tempInF - 32) * 5) / 9, '.1f')

def meanOfList(input: List):
    totalVal, totalNums = 0, 0
    for value in input:
        totalVal += value
    return totalVal / totalNums

def photosyntheticRateCalc(NDVI: int, SWdw: int):
    return NDVI * SWdw

def changeInNDVI(prevNDVI: int, currNDVI: int):
    return currNDVI - prevNDVI

# useful for precipitation lag
def sumThroughRange(input: List, rangeSize: int, startingIndex: int):
    total = 0
    for i in range(0, rangeSize + 1):
        total += input[startingIndex + i]
    return total

# useful for n-day avg NDVI
def avgThroughRange(input: List, rangeSize: int, startingIndex: int):
    total, numsAdded = 0, 0
    for i in range(0, rangeSize + 1):
        total += input[startingIndex + i]
    return total / numsAdded

def toBinary(input: bool):
    return 1 if input == True else 0