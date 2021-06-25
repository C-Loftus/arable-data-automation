
from typing import List

import serialNums
    
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
    if serialNumber in serialNums.private.hoopHouse:
        return "hoop house"
    else:
        return "open field"
