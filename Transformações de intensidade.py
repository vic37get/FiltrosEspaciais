import cv2
import numpy as np
import matplotlib.pyplot as plt


def Inversa(imagem):
    imagem = cv2.imread(imagem)
    for x in range(0,imagem.shape[0]):
        for y in range(0, imagem.shape[1]):
            imagem[x,y] = 255 - imagem[x,y]
    cv2.imshow("imagem-negativa", imagem)
    cv2.imwrite("inversa.png",imagem)
    cv2.waitKey(0)
    
    
def Logaritmica(imagem,c=None):
    imagem = cv2.imread(imagem)
    c = 255/np.log(1+255)
    for x in range(0,imagem.shape[0]):
        for y in range(0, imagem.shape[1]):
            imagem[x,y] =  c*np.log(1+imagem[x,y])
    cv2.imshow("Imagem de saída", imagem)
    cv2.imwrite("Logaritmica.png",imagem)
    cv2.waitKey(0)
    

def Exponencial(img,a=None):
    imagem = cv2.imread(img)
    if(a == None):
        a = 255/imagem.max()**np.e
    for x in range(0,imagem.shape[0]):
        for y in range(0, imagem.shape[1]):
            imagem[x,y] =  a*((imagem[x,y]**np.e)-1)
    cv2.imshow("Imagem de saída", imagem)
    cv2.imwrite("Exponencial.png",imagem)
    cv2.waitKey(0)