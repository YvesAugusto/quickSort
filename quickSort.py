from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
 
def geraLista(size):
    vector = []
    while size > 0:
        vector.append(size)
        size-=1
    return vector
  
def geraInversa(size):
  vector=list(range(size,1,-1))
  return vector

def geraOrdenado(size):
	return list(range(size))


def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", name='fig'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo Aleatório")
    #ax.plot(x,y2, label = "Melhor Tempo Decrescente")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

operacoes=[]

def quickSort(vector,begin=0,end=0):
  pivo = vector[int((begin+end)/2)]
	aux = begin
	final = end-1
	while(aux <= final):
		while(aux<end and vector[aux]<pivo):
			aux+=1
		while(final>begin and vector[final]>pivo):
			final-=1
		if final>=aux:
			vector[aux], vector[final] = vector[final],vector[aux]
      final-=1
			aux+=1
			
	if final>begin:
		quickSort(vector, begin, final+1)
	if aux<end:
		quickSort(vector, aux, end)

listas=[]
listaInversa=[]
listaOrdenada=[]
x2 = [100000, 200000, 400000, 500000, 1000000, 2000000]
y = []
y2=[]
y3=[]

for i in range(len(x2)):
  listas.append(geraLista(x2[i]))


for i in range(len(x2)):
  y.append(timeit.timeit("quickSort({})".format(listas[i]),setup="from __main__ import quickSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")


desenhaGrafico(x2,y,'Quantidade','Tempo', 'quickSort')
