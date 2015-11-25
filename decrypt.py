#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

#Imports
from PIL import Image
import quaternary   #quaternary.py
from quaternary import BaseFour
import rsa

def decrypt(fname,rsaKey):
    print 'Decrypting ' + fname + '...'
    
    f = open(fname, "r")
    fContents = f.read().split(".")
    fPix = fContents[1].split(",")
    fDimensions = fContents[0].split(",")
    imgwidth = int(fDimensions[0])
    imgheight = int(fDimensions[1])
    
    im = Image.new("RGB", (imgwidth, imgheight))
    pix = im.load()
    
    for x in range(imgwidth):
        if x == imgwidth / 4:
            print '25%'
        elif x == imgwidth / 2:
            print '50%'
        elif x == 3 * (imgwidth / 4):
            print '75%'
        row = fPix[(x*imgheight)-imgheight:x*imgheight]
        for y in range(len(row)):
            rgb = row[y].split('/')
            r_i = rsaKey.decryptBaseTen(int(rgb[0]))
            g_i = rsaKey.decryptBaseTen(int(rgb[1]))
            b_i = rsaKey.decryptBaseTen(int(rgb[2]))
        
            r_f = quaternary.intValToBaseFour(r_i)
            g_f = quaternary.intValToBaseFour(g_i)
            b_f = quaternary.intValToBaseFour(b_i)
        
            r = quaternary.toDecimal(r_f)
            g = quaternary.toDecimal(g_f)
            b = quaternary.toDecimal(b_f)
            
            
            #Print warnings if the decrypted RGB values are greater than 255
            if r > 255:
                print 'WARNING: r[' + str(x) + '][' + str(y) + ']=' + r
            if g > 255:
                print 'WARNING: g[' + str(x) + '][' + str(y) + ']=' + g
            if b > 255:
                print 'WARNING: b[' + str(x) + '][' + str(y) + ']=' + b
            
            rgb_n = (r,g,b)
            
            pix[x,y] = rgb_n
            
    fNameComp = fname.split(".")
    outfname = fNameComp[0]
    exten = fNameComp[1]
    im.show()
    im.save(outfname + "_OUTPUT" + exten)
    return fname