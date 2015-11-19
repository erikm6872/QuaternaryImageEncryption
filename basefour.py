#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

import math

class BaseFour(object):
    def __init__(self, dec):
        self.baseFourVals = self.fromDecimal(dec)   #Array containing base 4 value
        print self.baseFourVals #Print entire array (testing)
    
    #Convert from decimal to base 4
    def fromDecimal(self, dec):
        retArr = []  #Array containing base 4 value
        while dec > 3:  #dec := result
            retArr.insert(0,dec%4)   #Insert remainder into array
            dec = dec / 4                       #Update dec
        retArr.insert(0,dec) #Insert last value
        return retArr
    
    #Convert base 4 value back to base 10
    def toDecimal(self):
        retDec = 0
        for i in range(len(self.baseFourVals)):
            retDec = retDec + (self.baseFourVals[i] * math.pow(4, len(self.baseFourVals) - i - 1))
        return int(retDec)
        
