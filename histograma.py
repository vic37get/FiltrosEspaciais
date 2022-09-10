from matplotlib import pyplot as plt
import cv2
import numpy as np
import random


def ExibeHistInicial(imagem):
    img = cv2.imread(imagem)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    list = [img,hist]
    return list

def EqualizaHist(imagem):
    img = cv2.imread(imagem)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalizado = cv2.equalizeHist(img)
    hist_equalizado = cv2.calcHist([equalizado],[0],None,[256],[0,256])
    list = [equalizado,hist_equalizado]
    return list
    
  

def ExibeHists(hist,titulo):
    plt.title(titulo)
    plt.xlabel("Intensidade")
    plt.ylabel("Qtde de Pixels")
    plt.xlim([0, 256])
    plt.hist(hist,256,[0,256])

def ComparaHist(imagem,imagemesp,especificada):
    original = ExibeHistInicial(imagem)
    equalizada = EqualizaHist(imagem)
    plt.subplot(221), ExibeHists(original[1],"Imagem Original")
    plt.subplot(222), ExibeHists(equalizada[1], "Imagem Equalizada")
    plt.subplot(223), ExibeHists(especificada, "Imagem Especificada")
    plt.show()
    cv2.imshow("Imagem Equalizada", np.hstack((original[0], equalizada[0])))
    cv2.imshow('Especificada',imagemesp)
    cv2.imwrite('equalizada.jpg',equalizada[0])
    cv2.imwrite('especificada.jpg',imagemesp)
    cv2.waitKey(0)
    
def show_his(v,size=(6,4),l=255,title = ''):
        c = v
        plt.figure(figsize=(size[0],size[1]))
        plt.xlim([0,l])
        plt.title(title)
        plt.bar(list(range(0,256)),v,edgecolor="#1f77b4",color="#1f77b4")
        plt.show()

def histespecificado(imagem,imgclara):
    v = 0
    imagem = cv2.imread(imagem)
    l,a = imagem.shape[1], imagem.shape[0]
    quant_pixels = l*a
    lista = []
    for i in range(0,256):
        umQuarto = int(quant_pixels/5)
        if(imgclara == True):
            if(quant_pixels == 0):
                intervalo = 0
            elif(i%3 == 0):
                intervalo = random.randint(0,umQuarto)
                quant_pixels-=intervalo
            else:
                intervalo = 0
            lista.append(intervalo)
        if(imgclara == False):
            if(quant_pixels == 0):
                intervalo = 0
            if(i>=180):
                intervalo = random.randint(0,quant_pixels)
                quant_pixels-=intervalo
            else:
                intervalo = 0
            lista.append(intervalo)
    print(lista)
    return lista

def retorna_min(f, a):
    valor = 0
    contador = 0
    aux = []
    for i in range(len(a)):
        aux.append(abs(a[i]-f))
    menor = aux[0]
    for i in range(len(aux)-1):
        if(aux[i+1] < menor):
            menor = aux[i+1]
    for i in aux:
        if menor == i:
            valor = contador
            break
        contador += 1
    return a[contador]

#MAIN
#ESPECIFICADA
img = cv2.imread('bote.jpg',1)
foto = 'bote.jpg'
dimensao = np.shape(img)
vetor_associado = np.zeros(256)
vetor_teste = histespecificado(foto,True)

quantidade_de_pixels = 0
vetor_hist = np.zeros(256)
for i in range(0, dimensao[0]):
  for j in range(0, dimensao[1]):
    for k in range(0,dimensao[2]):
      f = img[i][j][k]
      vetor_hist[f] = vetor_hist[f] + 1
      quantidade_de_pixels = quantidade_de_pixels + 1

def CalculaProbabilidadeVetorHist(vetor_hist):
    vetor_probabilidade = []
    for i in vetor_hist:
        vetor_probabilidade.append((i/quantidade_de_pixels))
    return vetor_probabilidade

vetor_probabilidade = CalculaProbabilidadeVetorHist(vetor_hist)

def CalculaDistribuicaoVetorProb(vetor_probabilidade):
    vetor_novos_pixels = []
    guarda_somatorio = 0
    for i in vetor_probabilidade:
        guarda_somatorio = guarda_somatorio + (255*i)
        vetor_novos_pixels.append(guarda_somatorio)
    return vetor_novos_pixels

vetor_novos_pixels = CalculaDistribuicaoVetorProb(vetor_probabilidade)

def CalculaProbEspecificado(vetor_teste, quantidade_de_pixels):
    vetor_probabilidade_teste = []
    for i in vetor_teste :
        vetor_probabilidade_teste.append(i/quantidade_de_pixels)
    return vetor_probabilidade_teste

vetor_probabilidade_teste = CalculaProbEspecificado(vetor_teste,quantidade_de_pixels)

def CalculaVetorAcumulado(vetor_probabilidade):
    vetor_hist = []
    guarda_somatorio = 0
    for i in vetor_probabilidade:
        if(i!=0):
            guarda_somatorio = guarda_somatorio + i
            vetor_hist.append(guarda_somatorio)
    return vetor_hist

vetor_hist_teste = CalculaVetorAcumulado(vetor_probabilidade_teste)
vetor_acumulado_principal = CalculaVetorAcumulado(vetor_probabilidade)

def SoProbabilidade(vetor_probabilidade):
    vetor_somente_probabilidade = []
    for i in vetor_probabilidade:
        if i>0:
            vetor_somente_probabilidade.append(i)
    return vetor_somente_probabilidade

vetor_somente_probabilidade = SoProbabilidade(vetor_probabilidade)

def Mapeamento(vetor_acumulado_principal,vetor_hist_teste):
    vetor_associacao = []
    for i in range(len(vetor_acumulado_principal)):
        x = retorna_min(vetor_acumulado_principal[i], vetor_hist_teste)
        vetor_associacao.append([vetor_acumulado_principal[i],x])
    return vetor_associacao

vetor_associacao = Mapeamento(vetor_acumulado_principal,vetor_hist_teste)

def CalcAcumuladoEspec(vetor_probabilidade):
    somatorio = 0
    vetor_acumulada_real = []
    for i in vetor_probabilidade:
        somatorio += i
        vetor_acumulada_real.append(somatorio)
    return vetor_acumulada_real

vetor_acumulada_real = CalcAcumuladoEspec(vetor_probabilidade)
vetor_acumulada_real2 = CalcAcumuladoEspec(vetor_probabilidade_teste)


def IndexAssociado(vetor_associacao):
    vetor_index_associado = []
    for i in range(len(vetor_associacao)):
        vetor_index_associado.append([0, 0])
    return vetor_index_associado

vetor_index_associado = IndexAssociado(vetor_associacao)
        
def MapeiaVetores(vetor_associacao,vetor_acumulada_real,vetor_index_associado,k):
    for i in range(len(vetor_associacao)):
        for j in range(len(vetor_acumulada_real)):
            if (vetor_associacao[i][k] == vetor_acumulada_real[j]):
                vetor_index_associado [i][k] = j
    return vetor_index_associado

vetor_index_associado = MapeiaVetores(vetor_associacao,vetor_acumulada_real,vetor_index_associado,0) 
vetor_index_associado = MapeiaVetores(vetor_associacao,vetor_acumulada_real2,vetor_index_associado,1)

def find_associado(valor, vetor):
  for i in vetor:
    if(i[0]==valor):
      f = i[1]
      return f

for i in range(0, dimensao[0]):
 for j in range(0, dimensao[1]):
    for k in range(0,dimensao[2]):
      for l in vetor_index_associado:
        if(l[0]==img[i][j][k]):
          img[i][j][k] = l[1]
          break
Especificada = img.ravel()
plt.hist(Especificada,256,[0,256])
plt.show()
print('pronto!')
ComparaHist(foto,img,Especificada)
