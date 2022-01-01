#Numpy
#Maneras de crear arrays con numpy 
#Primero importamos numpy como np 
import numpy as np 

#Arreglo de enteros
np.array([1,4,2,5,3])

#Si los elementos del arreglo no son del mismo tipo numpy los toma como del tipo punto flotante
np.array([3.14, 4, 3, 4])

#Si queremos un tipo de dato especifico se utiliza dtype
np.array([1,2,3,4],dtype='float32')

#Para crear un arreglo de ceros se utiliza np.zeros indicando el numero de elementos y el tipo de dato
np.zeros(10,dtype=int)

#Para crear un arreglo de unos se utiliza donde el primer argumento es el tamaño del arreglo, el primer elemento es el numero de filas y el segundo el numero de columnas 
np.ones((3,5), dtype=float)

#Se pueden crear arreglos llenandolos con cualquier numero
np.full((3,5), 3.14)

#Se pueden crear arreglos llenandolos con una secuencia lineal por ejemplo que empiece desde 0 hasta 20 y que aumente de 2 en 2 
np.arange(0,20,2)

#Se pueden crear arreglos de cinco valores espaciados entre 0 y 1 
np.linspace(0,1,5)

#Se pueden crear arreglos con valores uniformemente distrivuidos entre 0 y 1  
np.random.random((3,3))

#Para crear valores normalmente distribuidos con media 0 y desviacion estandar 1
np.random.normal(0,1,(3,3))

#Para crear un arreglo de 3x3 de valores enteros aleatorios en un intervalo entre [0,10)
np.random.randint(0,10,(3,3))

#Para crear una matriz identidad
np.eye(3)

#Para crear un arreglo no inicializado de tres enteros, los valores seran lo que este en ese espacio de memoria
np.empty(6)

#Reshaping de arreglos
#La manera mas flexible de modificar la forma del arreglo es con reshape
grid = np.arange(1, 10).reshape((3, 3))
print(grid)

#Otra patron de conversion de formas de arreglos unidimensionales a bidimensionales o matrices de columnas

x = np.array([1, 2, 3])
x.reshape((1, 3)) #vector fila por reshape

array([[1, 2, 3]]) #vector fila por newaxis
x[np.newaxis, :]

x.reshape((3,1)) #Vector columna por reshape

x[:, np.newaxis] #Vector columna por newaxis

#Concatenacion y separacion de arreglos 
#Concatenar o unir arreglos en Numpy 
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.array([99, 99, 99])
np.concatenate([x,y,z])

#np.concatenate puede unir arreglos de dos dimensiones
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
np.concatenate([grid,grid])

#Tambien se puede concatener a lo largo del segundo eje
np.concatenate([grid,grid], axis=1)

#Se puede mezclar arreglos de distintas dimensiones con np.vstack (para apilar vertical) y np.hstack (apilar horizontal)

#Apilar vertical 
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

np.vstack([x, grid])

#Apilar horizontal 
y = np.array([[99],
              [99]])

np.hstack([grid, y])

#Separar arreglos
#Se pueden separar arreglos de manera vertical, horizontal o por una lista de indices 

x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5]) #3 y 5 son los puntos para la separacion
print(x1, x2, x3)


#Para separacion de arreglos de manera vertical 
grid = np.arange(16).reshape((4,4))
grid

upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

#Para separar arreglos de manera horizontal 

left, right = np.hsplit(grid, [2])
print(left)
print(right)

#Ufuncs 
#Las ufuncs son conocidas como operaciones vectorizadas las cuales trabajan mas rapido que las funciones de python 

#Las ufuncs se clasifican en dos tipos: unary ufuncs, que operan con una unica entrada, y binary ufuncs que operan con dos entradas. 

#Aritmetica en arreglos
#Ufuncs de Numpy se sienten muy naturales porque utilizan los operadores nativos de python. La suma, resta, multiplicacion y division estandar se pueden usar como:

x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x //2 =", x //2)
print("-x    =", -x)
print("x ** 2 =", x **2)
print("x % 2 =", x % 2)

#Los operadores aritmeticos tienen sus equivalentes en Numpy
#Los cuales son np.add, np.subtract, np.negative, np.multiply
#np.divide, np.floor_divide, np.power, np.mod

#Valor absoluto
#Algunas funciones de Python se pueden utilizar con los arreglos como 
#el valor absoluto, y Numpy tambien tiene su ufunc para el valor absoluto esta tambien puede devolver la magnitud de un numero complejo

x = np.array([-2, -1, 0, 1, 2])
abs(x)

np.absolute(x)
np.abs(x)

i = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
np.abs(i)


#Funciones trigonometricas 
#Numpy provee de muchas funciones que son muy utiles como las funciones trigonometricas

theta = np.linspace(0, np.pi, 3)

print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))
print("arcsin(theta) = ", np.arcsin(theta))
print("arccos(theta) = ", np.arccos(theta))
print("arctan(theta) = ", np.arctan(theta))

#Los valores son computados dentro de la precision de la maquina, por lo que los valores que deberian ser cero no son exactamente cero.


#Exponentes y logaritmos
#Otras de las funciones disponibles en Numpy como ufunc son las exponenciales y logaritmos. 

x =  [1, 2, 3]
print('x       =', x)
print('e^x     =', np.exp(x))
print('2^x     =', np.exp2(x))
print('3^x     =', np.power(3,x))


#Las funciones inversa de los exponenciales son los logaritmos

x = [1, 2, 4, 10]
print('x  =', x)
print('ln(x) =', np.log(x))
print('log2(x) =', np.log2(x))
print('log10(x) =', np.log10(x))

#Si se necesita precision se pueden utilizar las funcioens especializadas 

x = [0, 0.001, 0.01, 0.1]
print('exp(x)-1', np.expm1(x))
print('log(1+x)=', np.log1p(x))


#Funciones especializadas 
#Para ver mas funciones especiales se pueden revisar la documentacion
#Funciones como scipy.special las cuales contienen algunas funciones como special.gamma, special.gammaln, special.beta


#Presentacion avanzadas de Ufunc


#Especificar la salida
#Para algunos calculos largos se necesita especificar en donde se almacenara el resultado en vez de crear un arreglo temporal. 

x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)

#Tambien se puede especificar en cuales elementos del arreglo se quiereque se guarden los resultados por ejemplo en los elementos pares

y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)

