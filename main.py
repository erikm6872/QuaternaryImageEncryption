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
import os
import time

def main():
    #Control variables. Used for testing purposes. 
    #   If the RSA public and private key values are above ~2000, the encryption and decryption  
    #   calculations can take a very long time, especially on large image files.
    #If both vars are set False, the possible p and q values are between 373 and 997.
    smallprimes = True      #p and q between 101 and 367
    verysmallprimes = False  #p and q between 59 and 179
    
    #rsaTest() and rsa.verify() variables
    #   Both of these methods can take a very long time if smallprimes and verysmallprimes are set to False.
    vruns = 10
    numTestRuns = 50   #Number of loops to execute if `Run RSA test on current key` is selected
        
    
    if len(sys.argv) == 2:
        fname = sys.argv[1] 
        runAutoTest(fname)
    else:
        rsaGen = False
        done = False
        
        while done == False:
            op = int(displayMenu(smallprimes, verysmallprimes, vruns, numTestRuns))
            if op == 1:                                         #Generate RSA key
                rsaKey = rsa.RSA(smallprimes,verysmallprimes)
                rsaGen = True
                e,d,n = rsaKey.getKeys()
                print 'public key : ' + str(e)
                print 'private key: ' + str(d)
                print 'mod        : ' + str(n)
                print 'Press enter to continue...'
                raw_input("") #pause so that the keys can be seen
            elif op == 2:                                       #Import RSA key from file
                rsaKey = rsa.RSA(True,True)
                keyfname = raw_input("Enter key filename: ")
                keyFile = open(keyfname, "r")
                keys = keyFile.read().split("/")
                e = int(keys[0])
                d = int(keys[1])
                n = int(keys[2])
                print "Verifying RSA key pairs..."
                if rsa.verify(e,d,n,vruns) == True:
                    rsaKey.setKeys(e,d,n)
                    rsaGen = True
                    print ''
                    print "RSA key file \'" + keyfname + "\' successfully imported."
                    print ''
                    print 'public key : ' + keys[0]
                    print 'private key: ' + keys[1]
                    print 'mod        : ' + keys[2]
                    raw_input("Press enter to continue...") #pause so that the keys can be seen
                else:
                    printInvalidRSA()
            elif op == 3:                                       #Enter existing RSA key
                rsaKey = rsa.RSA(True,True)
                eIn = int(raw_input("Enter public key : "))
                dIn = int(raw_input("Enter private key: "))
                nIn = int(raw_input("Enter mod value  : "))
                print "Verifying RSA key pairs..."
                if rsa.verify(eIn,dIn,nIn,vruns) == True:
                    rsaKey.setKeys(eIn,dIn,nIn)
                    rsaGen = True
                    print "RSA keys set."
                    print 'Press enter to continue...'
                    raw_input("")
                else:
                    printInvalidRSA()
            elif op == 4:                                       #Save current key to file
                if rsaGen == True:
                    keyfname = raw_input("Enter filename for key: ")
                    keyDir = "keys/"
                    if not os.path.exists(keyDir): #Create `./keys/` directory if it doesn't already exist
                        os.makedirs(keyDir)
                    rsaKey.writeKeysToFile(keyDir + keyfname)
                else:
                    print "No RSA keys defined."
            elif op == 5:                                           #Encrypt image
                if rsaGen == True:
                    imageFile = raw_input("Enter image filename: ")
                    encfname = encrypt(imageFile,rsaKey,True,True)
                    print "Encrypted file saved to " + encfname
                    raw_input("Press enter to continue...")
                else:
                    print "No RSA keys defined."
            elif op == 6:                                           #Decrypt file
                if rsaGen == True:
                    encFile = raw_input("Enter encrypted file name: ")
                    decfname = decrypt(encFile,rsaKey,True,True)
                    if decfname != None:
                        print "Decrypted image saved to " + decfname
                        raw_input("Press enter to continue...")
                    else:
                        print "Decryption aborted."
                        print ''
                        raw_input("Press enter to continue...")
            elif op == 7:                                               #Run RSA test on currently loaded keys
                if rsaGen == True:
                    print "Verifying current RSA key..."
                    e,d,n = rsaKey.getKeys()
                    if rsa.verify(e,d,n,vruns) == True:
                        print "Done."
                        print ''
                        print "Testing quaternary encrypt/decrypt algorithm using current keys..." 
                        testRSA(rsaKey, numTestRuns)
                    else:
                        printInvalidRSA()
                else:
                    print "No RSA keys defined."
            elif op == 8:
                if rsaGen == True:
                    print "Verifying current RSA key..."
                    e,d,n = rsaKey.getKeys()
                    if rsa.verify(e,d,n,vruns) == True:
                        print "Done."
                        raw_input("Press enter to continue...")
                    else:
                        printInvalidRSA()
            elif op == 9:
                tests = int(raw_input("Number of tests: "))#100
                ind = 0
                #print 'Running ' + str(tests) + ' tests...'
                print ''
                keys = rsaGenerationTest(smallprimes, verysmallprimes, tests, ind)
                encryptTimes = encryptTimingTest("sample_401px.jpg", smallprimes, verysmallprimes, keys)
                #decryptTimes = decryptTimingTest("output/sample_160px")
                
                #for i in keys:
                #    print 'public key:  ' + str(i[0])
                #    print 'private key: ' + str(i[1])
                #    print 'mod: ' + str(i[2])
                #    print ''
                for i in encryptTimes:
                    print str(i[0]) + ", " + str(i[1]) + ", " + str(i[2])
                raw_input("Press enter to continue...")
            elif op == 10:            #Quit
                done = True
            else:                                           #Input is not a valid option (1-8)
                print "Invalid option selected."    
    
def displayMenu(smallprimes, verysmallprimes, vruns, numTestRuns):
    print ""
    print "**QuaternaryImageEncryption Menu**"
    print "*********Current Settings*********"
    print "smallprimes=" + str(smallprimes)
    print "verysmallprimes=" + str(verysmallprimes)
    print "vruns=" + str(vruns)
    print "numTestRuns=" + str(numTestRuns)
    print ""
    print "***********RSA Options************"
    print "1.  Generate new RSA key"
    print "2.  Import RSA key from file"
    print "3.  Enter existing RSA key manually"
    print "4.  Write current RSA keys to file"
    print ""
    print "**********Image Options***********"
    print "5.  Encrypt Image to .enc file"
    print "6.  Decrypt .enc file to image"
    print ""
    print "**********Other Options***********"
    print "7.  Test algorithm on current key"
    print "8.  Verify current RSA key"
    print "9.  RSA Generation test"
    print "10. Exit"
    print ""
    return raw_input(">")
def testRSA(rsaKey, numRuns):
    errors = 0
    for i in range(numRuns):
        m = random.randrange(0,255)
        mq = BaseFour(m)
        mqi = mq.getIntVal()
        c = rsaKey.encryptBaseTen(mqi)
        mpi = rsaKey.decryptBaseTen(c)
        mp = quaternary.intValToBaseFour(mpi)

        mf = quaternary.toDecimal(mp)
        #print 'Run  ' + str(i)
        #print 'm:   ' + str(m)
        #print 'mqi: ' + str(mqi)
        #print 'c:   ' + str(c)
        #print 'mpi: ' + str(mpi)

        #print 'mf:  ' + str(mf)
        if m != mf or mqi != mpi:
            print 'ERROR: m=' + str(m) + ', mf=' + str(mf)
            print 'ERROR: mqi=' + str(mqi) + ', mpi=' + str(mpi)
            #i = raw_input("")
            errors = errors + 1
        #print ''
    print "Test completed " + str(numRuns) + " runs with " + str(errors) + " errors"
    if errors > 0:
        print "RSA Key Values:"
        e,d,n = rsaKey.getKeys()
        print 'public key:  ' + str(e)
        print 'private key: ' + str(d)
        print 'mod: ' + str(n)
    print ''
    raw_input("Press enter to continue...")
def runAutoTest(fname):
    im = Image.open(fname)
    pix = im.load()
    
        #Get image dimensions
    imgsize = im.size
    imgwidth = imgsize[0]
    imgheight = imgsize[1]
    
    
    rsaKey = rsa.RSA(smallprimes,verysmallprimes)
    e,d,n = rsaKey.getKeys()
    print 'public key:  ' + str(e)
    print 'private key: ' + str(d)
    print 'mod: ' + str(n)
    print 'Press enter to continue...'
    raw_input("") #pause so that the keys can be seen by user
    print ''
    
    encryptedfname = encrypt(fname,rsaKey,True,True)
    print '**************'
    #decryptedfname = decrypt(encryptedfname,rsaKey,imgwidth,imgheight)
def printInvalidRSA():
    print ""
    print "***************************************************"
    print "ERROR: Key values provided are not valid RSA pairs."
    print ""
    print "Please check that key values are correct and enter"
    print "them again."
    print "***************************************************"
    raw_input("Press enter to continue...")
def rsaGenerationTest(smallprimes, verysmallprimes, numGens, sortBy):
    gens = []
    for i in range(numGens):
        gens.append([])
        e,d,n = rsa.RSA(smallprimes,verysmallprimes).getKeys()
        gens[i].append(e)
        gens[i].append(d)
        gens[i].append(n)
        
        #print 'public key:  ' + str(e)
        #print 'private key: ' + str(d)
        #print 'mod: ' + str(n)
        #print ''
    #print ""
    #print "sorted"
    #print ""
    
    gens.sort(key=lambda x: x[sortBy])
    
    #for i in gens:
    #    print 'public key:  ' + str(i[0])
    #    print 'private key: ' + str(i[1])
    #    print 'mod: ' + str(i[2])
    #    print ''
    
    return gens
def encryptTimingTest(fname, smallprimes, verysmallprimes, gens):
    
    rsaKey = rsa.RSA(smallprimes,verysmallprimes)
    
    encryptTimes = []
    
    for i in range(len(gens)):
        rsaKey.setKeys(gens[i][0], gens[i][1], gens[i][2])
        
        encryptTimes.append([])
        encryptTimes[i].append(gens[i][0])
        encryptTimes[i].append(gens[i][1])
        
        print("Run " + str(i+1) + "/" + str(len(gens)+1) + ": e = "+str(gens[i][0])+", d = "+str(gens[i][1])+", n = "+str(gens[i][2]))
        
        sTime = time.time()
        encrypt(fname,rsaKey,False,False)
        eTime = time.time() - sTime
        
        print "Elapsed time = " + str(eTime) + " s"
        print ''
        
        encryptTimes[i].append(eTime)
        
    return encryptTimes
    
def decryptTimingTest(fname, smallprimes, verysmallprimes, gens):
    
    rsaKey = rsa.RSA(smallprimes,verysmallprimes)
    
    decryptTimes = []
    
    for i in range(len(gens)):
        rsaKey.setKeys(gens[i][0], gens[i][1], gens[i][2])
        
        decryptTimes.append([])
        decryptTimes[i].append(gens[i][0])
        decryptTimes[i].append(gens[i][1])
        
        print(str(i+1) + ") e = "+str(gens[i][0])+", d = "+str(gens[i][1])+", n = "+str(gens[i][2]))
        #raw_input("start")
        
        sTime = time.time()
        decrypt(fname,rsaKey,False,False)
        eTime = time.time() - sTime
        
        print "Elapsed time = " + str(eTime) + " s"
        print ''
        
        decryptTimes[i].append(eTime)
        
    return decryptTimes
main()