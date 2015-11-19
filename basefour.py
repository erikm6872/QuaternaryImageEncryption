#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

import math

class BaseFour(object):
    def __init__(self, dec):
        self.baseFourVals = []
        while dec > 3:
            elem = self.divFour(dec)
            dec = elem[0]
            self.baseFourVals.append(elem[1])
        self.baseFourVals.append(dec)
        self.reverseArray()
        print self.baseFourVals
        
    def toDecimal(self):
        retDec = 0
        for i in range(len(self.baseFourVals)):
            retDec = retDec + (self.baseFourVals[i] * math.pow(4, len(self.baseFourVals) - i - 1))
        return int(retDec)
    
    def divFour(self, inVal):
        retArr = []
        retArr.append(inVal / 4)
        retArr.append(inVal % 4)
        return retArr
    def reverseArray(self):
        #print len(self.baseFourVals)
        for i in range(len(self.baseFourVals)/2):
            temp = self.baseFourVals[i]
            self.baseFourVals[i] = self.baseFourVals[len(self.baseFourVals) - i - 1]
            self.baseFourVals[len(self.baseFourVals) - i - 1] = temp