#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

#Imports
from PIL import Image
from random import *
import os

def main():
    fname = raw_input("fname=")
    encrypt(fname)

def encrypt(fname):

    #Open and load image file
    im = Image.open(fname)
    pix = im.load()
    
    #Get image dimensions
    imgsize = im.size
    imgwidth = imgsize[0]
    imgheight = imgsize[1]
        
    #   TODO: 
    #   1. Convert RGB values to base 4
    #   2. Encryption in base 4, possibly RSA
    #   3. Convert back to base 10
    
    #   What this does right now is just swap random pixels
    for x in range(0, imgwidth):
        for y in range(0, imgheight):
            rgb = pix[x,y]                          #Get array of RGB values - rgb[0] = red, etc
            avg = (rgb[0] + rgb[1] + rgb[2]) / 3    #If we wanted to convert to greyscale
            
            #Pick random pixel to swap
            x1 = randint(0, imgwidth-1)
            y1 = randint(0, imgheight-1)
            
            #Swap pixels
            pix[x,y] = pix[x1,y1]
            pix[x1,y1] = rgb

    im.show()   #Open produced image in default program (Windows Photo Viewer, Preview, etc)
    
    #Save generated image to directory ./output/<filename>.jpg
    outputFolder = 'output/'
    if not os.path.exists(outputFolder):    #Create ./output/ directory if it doesn't exist already
        os.makedirs(outputFolder)
    im.save(outputFolder + fname)   #Save to file
    print "Done."
main()