#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

#Imports
import sys
from encrypt import *
from decrypt import *
import rsa
import random
from quaternary import BaseFour
import quaternary
from PIL import Image

def main():
    #Control variables
    smallprimes = True
    verysmallprimes = True
    
    runRSATest = False
    numTestRuns = 1000
    
    
    
    #Set filename if passed as an argument
    #if len(sys.argv) == 3:
    #    fname = sys.argv[1]
    #    eArg = sys.argv[2]
    
    #If passing e as an arg is enabled, this should be an `elif` 
    if len(sys.argv) == 2:
        fname = sys.argv[1] 
        #eArg = -1
    else:
        print "Usage: image.py <filename>" #<public key>"
        #eArg = -1
        #Get filename to open - sample.jpg hardcoded for testing purposes
        fname = raw_input("fname=")
        #fname = 'sample.jpg' 
    
    im = Image.open(fname)
    pix = im.load()
    
    #Get image dimensions
    imgsize = im.size
    imgwidth = imgsize[0]
    imgheight = imgsize[1]
    
    
    rsaKey = rsa.RSA(-1,smallprimes,verysmallprimes)    #eArg)
    e,d,n = rsaKey.getKeys()
    print 'public key:  ' + str(e)
    print 'private key: ' + str(d)
    print 'mod: ' + str(n)
    print 'Press enter to continue...'
    raw_input("") #pause so that the keys can be seen
    print ''
    
    
    if runRSATest == True:
        testRSA(rsaKey, numTestRuns) #Test RSA encryption with `numRuns` random integers in [0,255]
    
    encryptedfname = encrypt(fname,rsaKey)
    decryptedfname = decrypt(encryptedfname,rsaKey,imgwidth,imgheight)
    
    
def testRSA(rsaKey, numRuns):
    for i in range(numRuns):
        m = random.randrange(0,255)
        mq = BaseFour(m)
        mqi = mq.getIntVal()
        c = rsaKey.encryptBaseTen(mqi)
        mpi = rsaKey.decryptBaseTen(c)
        mp = quaternary.intValToBaseFour(mpi)
        #mp = BaseFour(0)
        #mp.setVals(quaternary.intValToBaseFour(mpi))
        mf = quaternary.toDecimal(mp)
        print 'Run  ' + str(i)
        print 'm:   ' + str(m)
        print 'mqi: ' + str(mqi)
        print 'c:   ' + str(c)
        print 'mpi: ' + str(mpi)
        #print 'mp:  '
        #print  mp
        print 'mf:  ' + str(mf)
        if m != mf or mqi != mpi:
            print 'ERROR: m=' + str(m) + ', mf=' + str(mf)
            print 'ERROR: mqi=' + str(mqi) + ', mpi=' + str(mpi)
            i = raw_input("")
        print ''

main()