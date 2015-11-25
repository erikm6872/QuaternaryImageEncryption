#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

#Imports
from PIL import Image
from random import *
import os
import quaternary   #quaternary.py
from quaternary import BaseFour
import rsa

def encrypt(fname,rsaKey):

    #Open and load image file
    im = Image.open(fname)
    pix = im.load()
    
    #Get image dimensions
    imgsize = im.size
    imgwidth = imgsize[0]
    imgheight = imgsize[1]
    
    #   Step 2 given
    #   -------------
    #   1)  x_0 = 2
    #   2)  rule: x_k = (5x_(k-1)+1)_base4
    #       k>1 is given (a param)
    #   3)  x_1 = (2*2+1) = 5 = 1(base4)
    #   4)  x_2 = (2*x_1+1) = (2*1+1) = 3(base4)
    #       ...
    #   n)  x_k = 2 <-Scrambled value
    
    A = [['' for x in range(imgheight)] for x in range(imgwidth)]
    
    print 'Encrypting ' + fname + '...'
    for x in range(0, imgwidth):
        if x == imgwidth / 4:
            print '25%'
        elif x == imgwidth / 2:
            print '50%'
        elif x == 3 * (imgwidth / 4):
            print '75%'
        for y in range(0, imgheight):
           # print "[%d,%d]" % (x,y)
            rgb = pix[x,y]                          #Get array of RGB values - rgb[0] = red, etc
            avg = (rgb[0] + rgb[1] + rgb[2]) / 3    #If we wanted to convert to greyscale
            
            r = BaseFour(rgb[0])
            g = BaseFour(rgb[1])
            b = BaseFour(rgb[2])
            
            rd = rsaKey.encryptBaseTen(r.getIntVal())
            gd = rsaKey.encryptBaseTen(g.getIntVal())
            bd = rsaKey.encryptBaseTen(b.getIntVal())

            rgb_s = '%d/%d/%d' % (rd, gd, bd)
            A[x][y] = rgb_s

    #Save generated image to directory ./output/<filename>.jpg
    extension = '.enc'
    outputFolder = 'output/'
    if not os.path.exists(outputFolder):    #Create ./output/ directory if it doesn't exist already
        os.makedirs(outputFolder)
    outFile = outputFolder + fname + extension
    writeToFile(outFile, A, imgwidth, imgheight)    #Save to file
    print "Saved to " + outputFolder + fname + extension
    return outputFolder+fname+extension
    
def writeToFile(filename, A,imgwidth,imgheight):
    outFile = open(filename, "wb")
    outFile.write(str(imgwidth) + ","+str(imgheight)+"."+str(A).strip('[]').replace("'", '').replace(' ', '').replace('[', '').replace(']',''))
    outFile.close()