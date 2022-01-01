#Funciones básicas de Numpy

#Atributos de los arreglos de Numpy
#Primero vamos a definir tres arreglos: uno unidimensional, uno bidimensional y uno tridimensional

import numpy as np #Importamos la libreria de numpy con un alias 

np.random.seed(0) # Esta funcion genera una entrada para generar numeros pseudo aleatorios, cuando no se utiliza se generan numeros pseudo aleatorios diferentes

x1 = np.random.randint(10, size=6) #Arreglo de una dimension
x2 = np.random.randint(10,size=(3,4)) #Arreglo de dos dimensiones
x3 = np.random.randint(10,size=(3,4,5)) #Arreglo de tres dimensiones

print("x3 ndim:", x3.ndim) #.ndim nos da el numero de dimensiones del arreglo
print("x3 shape:", x3.shape) #.shape nos da la forma del arrglo
print("x3 size:", x3.size) #.size nos da el numero de elementos del arreglo 
print("dtype:", x3.dtype) #.dtype nos da el tipo de datos del arreglo
print("itemsize:", x3.itemsize, "bytes") #.itemsize nos da el tamaño de cada elemento del arreglo en bytes
print("nbytes:", x3.nbytes, "bytes") #.nbytes nos da el tamaño en bytes del arreglo

#Indice de los arreglos: Accediendo a elementos individuales
x1
x1[0] #Se puede acceder a cualquier valor del arreglo x[n] donde n es la posicion del arreglo 
x1[-3] #Se puede utilizar indices negativos, y se empieza a contar de derecha a izquierda 

x2
x2[0,1] #En arreglos de dos dimensiones se tiene que indicar la fila y la columna del elemento del arreglo, asi tambien para arreglos de tres dimensiones 

x2[0,1] = 6 #Se pueden modificar elementos asignandoles un valor al indice del elemento deseado,  hay que tomar en cuenta del tipo de dato del array

#Recortar arreglos: Accesando a subarreglos
#La manera de acceder a subarreglos es la siguiente
#x[inicio:fin:paso]

x = np.arange(10)

x[:5] #Primeros 5 elementos 
x[5:] #Ultimos 5 elementos 
x[4:7] #Elementos del 4 a 7
x[::2] #Los elementos pares 
x[1::2] #Los elementos de 2 en 2 empezando desde el elemento 1

#Los pasos pueden ser negativos, en este caso los valores de 
#inicio y paro se invierten, esta es una forma conveniente de invertir un arreglo 

x[::-1]
x[5::-2]

#Para arreglos multidimensionales se utiliza la misma nomenclatura
#separando por ,(comas) por ejemplo
x2[:2, :3] #Dos filas, tres columnas 
x2[:3, ::2] #Todas las filas, cada dos columnas 
x2[::-1,::-1] #Para invertir las columnas y las filas

#Una rutina necesaria comun es acceder a una sola columna o una sola fila de un arreglo
#Esto se puede hacer combinando los indices y los recortes, 
#usando un recorte vacio marcado por dos puntos

print(x2[:, 0]) #Primera columna de x2
print(x2[0,:]) #Primera fila de x2
print(x2[0]) #En caso de filas se puede acceder omitiendo el recorte

#Algo muy importante a tomar en cuenta que el slice en numpy nos devuelve vistas del arreglo no copias, por lo cual si se modifican los slice, se modifican el arreglo original 

print(x2)
x2_sub = x2[:2, :2]

x2_sub[0,0] = 99 

print(x2)

#Para crear copias de arreglos se utilza el metodo copy()

x2_sub_copy = x2[:2, :2].copy()

#Si se modifica el subarreglo, no se modifica el arreglo del que se hizo slice



