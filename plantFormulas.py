
from typing import List

def toFTemp(tempInF: int):
    return ((9/5)*(tempInF))+32

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