#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

import math
import random
import quaternary

class RSA(object):
    def __init__(self,smallprimes,verysmallprimes):
        p, q = generatePrimes(smallprimes,verysmallprimes)
        self.n = p * q
        self.e,self.d, self.n = generateKeys(p,q)

    def setKeys(self, e, d, n):
        self.e = e
        self.d = d
        self.n = n
    def getKeys(self):
        return (self.e, self.d, self.n)
        
    def encryptBaseTen(self, m):
        c = pow(m, self.e) % self.n
        return c
    
    def decryptBaseTen(self, c):
        return pow(c, self.d) % self.n
    
    def writeKeysToFile(self, fname):
        outFile = open(fname, "wb")
        outFile.write(str(self.e)+"/"+str(self.d)+"/"+str(self.n))
        outFile.close()
        print ''
        print "Wrote RSA keys to " + fname
        raw_input("Press enter to continue...")

        
    def encryptBaseFour(self, arr):
        dec = quaternary.toDecimal(arr)
        c = pow(dec, self.e) % 255
        retArr = quaternary.fromDecimal(c)
        return retArr

def generatePrimes(smallprimes, verysmallprimes):
    
    if smallprimes == True:
        if verysmallprimes == True:
            primes = [59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179]
            #[3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        else:
            primes = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                     ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                     ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367]
    else:
        primes =   [373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
                   
                   
                   
    #print 'Generating prime numbers...'
    p = primes[random.randrange(0, len(primes)-1)]
    q = primes[random.randrange(0, len(primes)-1)]
    while p == q:
        q = primes[random.randrange(0, len(primes)-1)]
    return (p,q)
def generateKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi-1)
    d = modinverse(e,phi)
    return (e,d,n)
    
##  Checks that provided RSA public, private, and mod values are valid.  
def verify(e,d,n,runs):
    for run in range(runs):
        i = random.randrange(0,255)
        c = pow(i,e) % n
        m = pow(c,d) % n
        if m != i:
            return False
    return True
def gcd(a,b):
    c = a % b
    if c == 0:
        return b
    else:
        return gcd(b,c)
        
def extendedGCD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extendedGCD(b % a, a)
        return (g, x - (b // a) * y, y)

def modinverse(a, m):
    g, x, y = extendedGCD(a, m)
    if g != 1:
        raise Exception('Invalid key values')
    else:
        return x % m