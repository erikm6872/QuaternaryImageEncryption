#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

#Imports
from PIL import Image
import quaternary   #quaternary.py
from quaternary import BaseFour
import rsa

def decrypt(fname,rsaKey,imgwidth,imgheight):
    print 'Decrypting ' + fname + '...'
    im = Image.new("RGB", (imgwidth, imgheight))
    pix = im.load()
    
    f = open(fname, "r")
    fContents = f.read()
    fPix = fContents.split(",")
    
    for x in range(imgwidth):
        if x == imgwidth / 4:
            print '25%'
        elif x == imgwidth / 2:
            print '50%'
        elif x == 3 * (imgwidth / 4):
            print '75%'
        row = fPix[(x*imgheight)-imgheight:x*imgheight]
        for y in range(len(row)):#imgheight):
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
            
            rgb_n = (r,g,b)
            #print rgb_n
            
            pix[x,y] = rgb_n
    
    #for i in range(len(fPix)):
    #    rgb = fPix[i].split('/')
        
    #    r_i = rsaKey.decryptBaseTen(rgb[0])
    #    g_i = rsaKey.decryptBaseTen(rgb[1])
    #    b_i = rsaKey.decryptBaseTen(rgb[2])
    #    
    #    r_f = quaternary.intValToBaseFour(r_i)
    #    g_f = quaternary.intValToBaseFour(g_i)
    #    b_f = quaternary.intValToBaseFour(b_i)
        
    #    r = quaternary.toDecimal(r_f)
    #    g = quaternary.toDecimal(g_f)
    #    b = quaternary.toDecimal(b_f)
        
    #    pix[x][y]
    im.show()
    ##Todo: Implement decryption algorithm
    return fname