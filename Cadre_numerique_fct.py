from PIL import Image, ImageTk
import sys
import numpy as np

def resize_fit_to_screen(fen, img):
    ratio = img.width/img.height
    fen_ratio = fen.width/fen.height
    if fen_ratio>ratio :
        img = img.resize((int(fen.height*ratio),fen.height),Image.BICUBIC, None, 100.0)
    else :
        img = img.resize((fen.width,int(fen.width/ratio)),Image.BICUBIC,None, 100.0)
    
    mat = img.load
    i=0
    j=0
    print (mat.size)


    return img