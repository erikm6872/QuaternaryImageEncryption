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
    verysmallprimes = True #Enabling `verysmallprimes` can sometimes mess with the RSA algorithm
    
    runRSATest = False
    numTestRuns = 1000
    
    
    if len(sys.argv) == 2:
        fname = sys.argv[1] 
        im = Image.open(fname)
        pix = im.load()
    
        #Get image dimensions
        imgsize = im.size
        imgwidth = imgsize[0]
        imgheight = imgsize[1]
    
    
        rsaKey = rsa.RSA(smallprimes,verysmallprimes)    #eArg)
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
        print '**************'
        decryptedfname = decrypt(encryptedfname,rsaKey,imgwidth,imgheight)
    else:
        rsaGen = False
        done = False
        
        while done == False:
            op = displayMenu()
            if op == 1:
                rsaKey = rsa.RSA(smallprimes,verysmallprimes)
                rsaGen = True
                e,d,n = rsaKey.getKeys()
                print 'public key:  ' + str(e)
                print 'private key: ' + str(d)
                print 'mod: ' + str(n)
                print 'Press enter to continue...'
                raw_input("") #pause so that the keys can be seen
            elif op == 2:
                rsaKey = rsa.RSA(smallprimes,verysmallprimes)
                eIn = int(raw_input("Enter public key : "))
                dIn = int(raw_input("Enter private key: "))
                nIn = int(raw_input("Enter mod value  : "))
                rsaKey.setKeys(eIn,dIn,nIn)
                rsaGen = True
                print "RSA keys set"
            elif op == 3:
                if rsaGen == True:
                    keyfname = raw_input("Enter filename for key: ")
                    rsaKey.writeKeysToFile("output/" + keyfname)
                else:
                    print "No RSA keys defined."
            elif op == 4:
                if rsaGen == True:
                    imageFile = raw_input("Enter image filename: ")
                    encryptedfname = encrypt(imageFile,rsaKey)
                else:
                    print "No RSA keys defined."
            elif op == 5:
                if rsaGen == True:
                    encFile = raw_input("Enter encrypted file name: ")
                    decryptedfname = decrypt(encFile,rsaKey)
            elif op == 6:
                if rsaGen == True:
                    testRSA(rsaKey, numTestRuns)
                else:
                    print "No RSA keys defined."
            elif op == 7:
                done = True
            else:
                print "Invalid option selected."
    
    #Set filename if passed as an argument
    #if len(sys.argv) == 3:
    #    fname = sys.argv[1]
    #    eArg = sys.argv[2]
    
    #If passing e as an arg is enabled, this should be an `elif` 
    
        #print "Usage: image.py <filename>" #<public key>"
        #eArg = -1
        #Get filename to open - sample.jpg hardcoded for testing purposes
        #fname = raw_input("fname=")
        #fname = 'sample.jpg' 
    
    
    
def displayMenu():
    print "ImageEncryption"
    print ""
    print "***********RSA Options************"
    print "1. Generate RSA key"
    print "2. Enter existing RSA key"
    print "3. Write current RSA keys to file"
    print ""
    print "**********Image Options***********"
    print "4. Encrypt Image to .enc file"
    print "5. Decrypt .enc file to image"
    print ""
    print "**********Other Options***********"
    print "6. Run RSA test"
    print "7. Exit"
    print ""
    return int(raw_input(">"))
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