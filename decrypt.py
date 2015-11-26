#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

#Imports
from PIL import Image
import quaternary   #quaternary.py
from quaternary import BaseFour
import rsa

def decrypt(fname,rsaKey):
    print("Decrypting " + fname + "..."),
    
    f = open(fname, "r")
    fContents = f.read().split(".")
    fPix = fContents[1].split(",")
    fDimensions = fContents[0].split(",")
    imgwidth = int(fDimensions[0])
    imgheight = int(fDimensions[1])
    
    im = Image.new("RGB", (imgwidth, imgheight))
    pix = im.load()
    
    error = False
    
    tenpercent = imgwidth / 10
    
    for x in range(imgwidth):
    
        printPercentage(x, tenpercent)
        
        row = fPix[(x*imgheight)-imgheight:x*imgheight]
        for y in range(len(row)):
            rgb = row[y].split('/')
            #print "(" + str(x) + "," + str(y) + ")="+rgb[0]+","+rgb[1]+","+rgb[2]
            #for i in rgb:
            #    if i == '':
            #        i = '0'
            r_i = rsaKey.decryptBaseTen(int("0x" + rgb[0],16))
            g_i = rsaKey.decryptBaseTen(int("0x" + rgb[1],16))
            b_i = rsaKey.decryptBaseTen(int("0x" + rgb[2],16))
        
            r_f = quaternary.intValToBaseFour(r_i)
            g_f = quaternary.intValToBaseFour(g_i)
            b_f = quaternary.intValToBaseFour(b_i)
        
            r = quaternary.toDecimal(r_f)
            g = quaternary.toDecimal(g_f)
            b = quaternary.toDecimal(b_f)
            
            
            if r > 255 or g > 255 or b > 255:
                print ''
                print ''
                print "****************ERROR*****************"
                print "Decrypted RGB values greater than 255 "
                print "RSA  key is probably incorrect.       "
                print "**************************************"
                print ''
                return None
            
            rgb_n = (r,g,b)
            
            pix[x,y] = rgb_n
            
    fNameComp = fname.split(".")
    outfname = fNameComp[0]
    exten = fNameComp[1]
    im.show()
    im.save(outfname + "_OUTPUT." + exten)
    return outfname + "_OUTPUT." + exten
def printPercentage(x, tenpercent):
    if x == tenpercent:
            print("10%"),
    elif x == tenpercent * 2:
        print("20%"),
    elif x == tenpercent * 3:
        print("30%"),
    elif x == tenpercent * 4:
        print("40%"),
    elif x == tenpercent * 5:
        print("50%"),
    elif x == tenpercent * 6:
        print("60%"),
    elif x == tenpercent * 7:
        print("70%"),
    elif x == tenpercent * 8:
        print("80%"),
    elif x == tenpercent * 9:
        print("90%")