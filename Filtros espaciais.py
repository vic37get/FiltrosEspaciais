import cv2
import numpy as np
import matplotlib.pyplot as plt


def FiltroMedia(imagem, mascarax, mascaray):
    imagem = cv2.imread(imagem)
    imagem_suavizada = cv2.blur(imagem, (mascarax, mascaray))
    cv2.imshow("Imagem Original", imagem)
    cv2.imshow("Imagens suavizada", imagem_suavizada)
    cv2.imwrite("ImagemFiltroMedia.jpg",imagem_suavizada)
    cv2.waitKey(0)
    
def FiltroMediana(imagem, mascara):
    imagem = cv2.imread(imagem)
    imagem_suavizada = cv2.medianBlur(imagem, (mascara))
    cv2.imshow("Imagem Original", imagem)
    cv2.imshow("Imagens suavizada", imagem_suavizada)
    cv2.imwrite("ImagemFiltroMediana.jpg",imagem_suavizada)
    cv2.waitKey(0)
    
def FiltroMediaPonderada(imagem, mascarax, mascaray):
    imagem = cv2.imread(imagem)
    imagem_suavizada = cv2.GaussianBlur(imagem, (mascarax, mascaray),0)
    cv2.imshow("Imagem Original", imagem)
    cv2.imshow("Imagens suavizada", imagem_suavizada)
    cv2.imwrite("ImagemFiltroMediaPonderada.jpg",imagem_suavizada)
    cv2.waitKey(0)
    
#FiltroMedia("ruido.png",5,5)
#FiltroMediana("ruido.png",3)
FiltroMediaPonderada("ruido.png",5,5)

