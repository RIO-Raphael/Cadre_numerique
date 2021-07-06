import sys
import random
from PySide6 import *
import numpy as np
import scipy.signal as sc

def resize_fit_to_screen(fen, img):
    ratio = img.width/img.height
    fen_ratio = fen.width/fen.height

    if fen_ratio>ratio :
        img = img.resize((int(fen.height*ratio),fen.height),Image.BICUBIC, None, 3)
    else :
        img = img.resize((fen.width,int(fen.width/ratio)),Image.BICUBIC,None, 3)
    
    noyau = np.array([[0, -0.1, 0],[-0.1, 1.5, -0.1],[0, -0.1, 0]])
    Filtre_convo(noyau, img)

    return img

def Filtre_convo(noyau, img):
    i=0
    j=0
    size = img.size
    mat_px = img.load()
    R = np.zeros(size)
    G = np.zeros(size)
    B = np.zeros(size)

    print ("traitement de l'image en cours ...")

    while (i < size[0]):
        j=0
        while (j < size[1]):
            R[i,j] = mat_px[i,j][0]
            G[i,j] = mat_px[i,j][1]
            B[i,j] = mat_px[i,j][2]
            j += 1
        i += 1

    print ("Division en matrices RGB ok.")

    R = sc.fftconvolve(noyau, R)
    G = sc.fftconvolve(noyau, G)
    B = sc.fftconvolve(noyau, B)

    print ("Convolution ok.")

    i=0
    while (i < size[0]):
        j=0
        while (j < size[1]):
            if (R[i,j]>255):
                R[i,j]=255
            if (G[i,j]>255):
                G[i,j]=255
            if (B[i,j]>255):
                B[i,j]=255
            if (R[i,j]<0):
                R[i,j]=0
            if (G[i,j]<0):
                G[i,j]=0
            if (B[i,j]<0):
                B[i,j]=0
            mat_px[i,j] = (int(R[i,j]),int(G[i,j]),int(B[i,j])) 
            j += 1
        i += 1
    
    print ("traitement de l'image fini !")

    return img