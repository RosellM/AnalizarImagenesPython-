
import random

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]

    return sum/len(lista)

def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print nombre + "[" + str(i) + "]=" + str(lista[i])

def leerLista():
    lista=[-1.99877399,
-2.67841158e-07,
0.00279341,
-5.52548785e-10,
-1.99999237,
1.48058115e-06,
1.99999929,
0.0632903,
0.07252775,
-0.37626627,
 2,
1.9805054,
-1.99999646,
1.12257145,
1.58850001e-05,
-1.99007084,
-0.57974573,
0.43227907,
-2,
0.0035774]
    return lista
A=leerLista()
imprimirLista(A,"A")
print "Promedio = " + str(promediarLista(A))
