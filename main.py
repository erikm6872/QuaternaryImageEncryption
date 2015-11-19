#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

#Imports
from encrypt import *
from decrypt import *
def main():

    #Get filename to open - sample.jpg hardcoded for testing purposes
    
    #fname = raw_input("fname=")
    fname = 'sample.jpg' 
    
    encryptedfname = encrypt(fname)
    decryptedfname = decrypt(fname)
    
    
main()