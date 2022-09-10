import cv2
import numpy as np
import matplotlib.pyplot as plt


def ExibeHistColorido(imagem):
    img = cv2.imread(imagem)
    cv2.imshow("Imagem Colorida", img)
    canais = cv2.split(img)
    cores = ("b", "g", "r")
    plt.figure()
    plt.title("Histograma Colorido")
    plt.xlabel("Intensidade")
    plt.ylabel("Número de Pixels")
    for (canal, cor) in zip(canais, cores):
        hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
        plt.plot(hist, cor)
        plt.xlim([0, 256])
    plt.show()

def EqualizaHistColorido(imagem):
    imagem = cv2.imread(imagem)
    imagemGray = cv2.cvtColor(imagem,cv2.COLOR_BGR2YUV)
    imagemGray[:,:,0] = cv2.equalizeHist(imagemGray[:,:,0])
    imagemEqualizada = cv2.cvtColor(imagemGray, cv2.COLOR_YUV2BGR)
    canais = cv2.split(imagemEqualizada)
    cores = ("b", "g", "r")
    plt.figure()
    plt.title("Histograma colorido equalizado")
    plt.xlabel("Intensidade")
    plt.ylabel("Número de Pixels")
    for (canal, cor) in zip(canais, cores):
        hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
        plt.plot(hist, cor)
        plt.xlim([0, 256])
    plt.show()
    cv2.imshow("Imagem Equalizada", np.hstack((imagem, imagemEqualizada)))
    cv2.imwrite("Imagem Equalizada.jpg", np.hstack((imagem, imagemEqualizada)))
    cv2.waitKey(0)
        
EqualizaHistColorido('paisagem.jpg')
#ExibeHistColorido('paisagem.jpg')