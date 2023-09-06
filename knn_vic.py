import pandas as pd
import math
import collections
import matplotlib.pyplot as plt


# Se crea un dataframe con el csv
df = pd.read_csv('./files/example3.csv')

#Se crea una lista de listas
c = [list(row) for row in df.values]


def euclidiana(a,b):                    #listas de coordenadas como parámetros de entrada, a es el punto ya clasificado y b por clasificar
    sum=0
    sum2 = [i for i in range(1)]
   
    for i in range(len(b)):
        sum += math.pow(a[i]-b[i], 2)   #suma de las diferencias al cuadrado

    sum2[0] = math.sqrt(sum)            #raiz cuadrada de la sumatoria  
    sum2.append(a[2])                   #Se agrega la clase del punto clasificado a la distancia 
    return sum2



def ordenar(distancias):
    
    n= len(distancias)-1

    for i in range(len(distancias)-1):
        for j in range(n):
            if distancias[j] > distancias[j+1]:
                a=distancias[j]
                distancias[j]=distancias[j+1]
                distancias[j+1]=a   
            n-1

def vecinosCercanos(k,d):
    
    cercanos=[i for i in range(k)] 

    for i in range(k):
        cercanos[i] = d[i]
    return cercanos 


def claseMay(vecinos):        #Se recibe una lista con las distancias y la clase de cada punto

    clases=[i for i in vecinos]  

    for i in range(len(vecinos)):
        clases[i]= vecinos[i][-1]   #Se sacan las clases y se guardan en una lista
    
    clase=collections.Counter(clases).most_common() #Se cuentan las pcurrencias de las clases que hay en la lista "clases" ordenados de mayor a menor
    
    return clase[0][0]  #Regresa la clase que tiene más ocurrencias


#KNN (SE LLAMA A LOS DEMAS METODOS)

def knn(puntoNuevo, puntosExistentes):
    d= [i for i in range(len(puntosExistentes))]
    vc=[]
    nuevo=[]
    for i in range(len(puntoNuevo)):
        for j in range(len(puntosExistentes)):
            d[j]= euclidiana(puntosExistentes[j],puntoNuevo[i]) #Se saca la distancia euclidiana

        ordenar(d) #Se ordena la lista de coordenadas    
        
        vc=vecinosCercanos(3,d) #Se sacan los k vecinos mas cercanos

        clase = claseMay(vc)    #Se elige la clase a la que pertenece

        # Lo que hago aqui es que voy almacenando todas las nuevas clasificaciones,
        # es decir, si tienes mas de 1 punto, retorno un lista con la clasificacion
        # de todos los puntos nuevos.
        nuevo.append(clase)

    return nuevo


if __name__ == '__main__':
    s = [[4,2]]

    dots_2d = [
        [4,5], 
        [18,20], 
        [12,10],
        [5,5],
        [13,15.2],
        [18,1],
        [17,2],
    ]

    print(knn([[4,5]], c))
