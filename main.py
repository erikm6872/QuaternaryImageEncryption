#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

#Imports
import sys
from encrypt import *
from decrypt import *

def main():
    
    #Set filename if passed as an argument
    if len(sys.argv) == 2:
        fname = sys.argv[1] 
    else:
        print "Usage: image.py <filename>"
        
        #Get filename to open - sample.jpg hardcoded for testing purposes
        fname = raw_input("fname=")
        #fname = 'sample.jpg' 

    encryptedfname = encrypt(fname)
    decryptedfname = decrypt(fname)
    
main()