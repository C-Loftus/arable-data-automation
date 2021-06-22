
from typing import List
from collections import defaultdict

import serialNums


class data:
    farms = {
                "CG" : "Cherry Grove",
                "AA": " Abe's Acres",
                "OO": "Orchard Organics", 
                "BRF": "Big Red Farm",
                "TS" : "Isles"
        }

    hoopHouse = ["A001505", "A001683", "C003649", "C003679"]

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
                "growing_environment": 2,
                "local_device_time" : 3,
                "julian_date": 4,
                "device" : 5, 
                "T_base": 6,
                "gdd": 7,
                "cgdd":8,
                "observed_growth": 9,
                "estimated_growth": 10,
                "cl" : 11,
                "NDVI" : 12,
                "ETc" :13,
                "SWdw": 14,
                "cmax_temp": 15,  # celcius
                "cmean_temp": 16, # celcius
                "cmin_temp": 17, # celcius
                "precip": 18,
                "max_temp": 19,  # f
                "mean_temp": 20, # f
                "min_temp": 21, # f,
                "photosynthetic_rate": 22,
                "crop_water_demand": 23,
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
                31 : "crop_water_demand"
            }

    both = ["local_device_time", "device", 
            "cl", "NDVI", "ETc", "SWdw", "max_temp", 
            "mean_temp", "min_temp", "precip", 
            "crop_water_demand"]


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

def photosyntheticRateCalc(NDVI, SWdw):
    try:
        NDVI = float(NDVI)
        SWdw = float(SWdw)
    except:
        return None
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

def environment(serialNumber):
    if serialNumber in data.hoopHouse:
        return "hoop house"
    else:
        return "open field"
