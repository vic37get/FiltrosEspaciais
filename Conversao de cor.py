import cv2
import matplotlib as mlt
import numpy as np


def ConverteCor(saida, imagem):
    imagemE = cv2.imread(imagem)
    if(saida == 'RGB'):
        imagemS = cv2.cvtColor(imagemE, cv2.COLOR_HSV2RGB)
        cv2.imshow('Imagem de saida', imagemS)
        cv2.imwrite('ImagemRGB.png', imagemS)
    else:
        imagemS = cv2.cvtColor(imagemE, cv2.COLOR_RGB2HSV)
        cv2.imshow('Imagem de saida', imagemS)
        cv2.imwrite('ImagemHSV.png', imagemS)
        

def ConvertePretoEbranco(imagem):
    imagemE = cv2.imread(imagem)
    imagemS = cv2.cvtColor(imagemE, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Imagem de saida', imagemS)
    cv2.imwrite('ImagemP&B.png', imagemS)
    
    
def ExibeCanalDeCor(imagem):
    image = cv2.imread(imagem)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    vermelho = image[:, :, 0]
    verde = image[:, :, 1]
    azul = image[:, :, 2]

    cv2.imshow('canal-vermelho', vermelho)
    cv2.imwrite('canal-vermelho.jpg', vermelho)
    
    cv2.imshow('canal-verde', verde)
    cv2.imwrite('canal-verde.jpg', verde)
    
    cv2.imshow('canal-azul', azul)
    cv2.imwrite('canal-azul.jpg', azul)

    

#ExibeCanalDeCor('arara.jpg')
#cv2.waitKey(0)
#cv2.destroyAllWindows()
 
 