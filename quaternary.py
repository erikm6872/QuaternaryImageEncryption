#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

import math
import random

class BaseFour(object):
    def __init__(self, dec):
        self.baseFourVals = fromDecimal(dec)   #Array containing base 4 value
        self.intVal = intValue(self.baseFourVals)

    #Convert base 4 value back to base 10 (class)
    def toDecimal(self):
        retDec = 0
        for i in range(len(self.baseFourVals)):
            retDec = retDec + (self.baseFourVals[i] * pow(4, len(self.baseFourVals) - i - 1))
        return int(retDec)
        
    def getVals(self):
        return self.baseFourVals
    def setVals(self, inArr):
        self.baseFourVals = inArr
    def getIntVal(self):
        return self.intVal

def intValToBaseFour(val):
    retArr = []
    while val > 0:
        retArr.insert(0,val % 10)
        val = int(math.floor(val / 10))
    return retArr
    
    
def intValue(arr):
    power = pow(10, len(arr)-1)
    retVal = 0
    for i in range(len(arr)):
        retVal = retVal + (arr[i] * power)
        power = power / 10
    return retVal
    
#Convert from decimal to base 4
def fromDecimal(dec):
    retArr = []  #Array containing base 4 value
    while dec > 3:  #dec := result
        retArr.insert(0,dec%4)   #Insert remainder into array
        dec = dec / 4                       #Update dec
    retArr.insert(0,dec) #Insert last value
    return retArr
    
#Convert base 4 value back to base 10 (generic)
def toDecimal(arr):
    retDec = 0
    for i in range(len(arr)):
        retDec = retDec + (arr[i] * pow(4, len(arr) - i - 1))
    return int(retDec)
    

