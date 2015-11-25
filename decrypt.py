#Erik McLaughlin
#11/18/2015
#https://github.com/erikm6872/QuaternaryImageEncryption

#Imports
from PIL import Image
import quaternary   #quaternary.py
from quaternary import BaseFour
import rsa

def decrypt(fname,rsaKey):#,imgwidth,imgheight):
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
            
            if r > 255:
                print 'WARNING: r[' + str(x) + '][' + str(y) + ']=' + r
            if g > 255:
                print 'WARNING: g[' + str(x) + '][' + str(y) + ']=' + g
            if b > 255:
                print 'WARNING: b[' + str(x) + '][' + str(y) + ']=' + b
            
            rgb_n = (r,g,b)
            #print rgb_n
            
            pix[x,y] = rgb_n
            
            
            #if x > 0 and y > 0:
            #    if ((pix[x,y][0] + pix[x,y][1] + pix[x,y][2]) - (pix[x-1,y-1][0] + pix[x-1,y-1][1] + pix[x-1,y-1][2])) > 250:
            #        print 'Large color shift at ['+ str(x) + '][' + str(y) + ']'
    
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