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

#Agregados
#Existen algunos agregados interesantes que pueden ser computados diretamente a los objetos. 
#Por ejemplo si se quiere reducir un arreglo con alguna operacion, se puede utilizar
#el metodo para cualquier ufunc.

x = np.arange(1,6)
np.add.reduce(x) #Se suman los elementos del arreglo 

np.multiply.reduce(x) #Se multiplican los elementos del arreglo 

np.add.accumulate(x) #Se se quiere almacenar resultados intermecios se puede
np.multiply.accumulate(x)

#Outer products
#Esta funcion permite operar cada par de elemento de dos entradas.

x = np.arange(1,6)
np.multiply.outer(x,x)

#Minimos, maximos y todo lo que se encuentra en medio

#Para sumar todos los valores de un arreglo 
L = np.random.random(100)
np.sum(L) #Se puede utilizar solo sum(L) pero como ya se menciono Numpy realiza las operaciones de una manera mas rapida

#Minimos y maximos 
big_array = np.random.rand(100000)
np.min(big_array), np.max(big_array) #Tambien existen las funciones min() y max()

#Una de las operaciones comunes es sumar los elementos de alguna columna o fila
M = np.random.random((3,4))
print(M)

M.sum()

M.min(axis=0) # (axis=0) regresa los valores de cada columna

M.max(axis=1) # (axis=1) regresa los valores de cada fila 

#Existen otras funciones de agregado las funciones np.nansum, np.nanprod
# estas funciones operan el arreglo ignorando los resultados los valores faltantes NaN

#Ver tabla 2-3 Aggregation functions available in Numpy

#Ejemplo pagina 61 

#Computation on arrays: Broadcasting

#Broadcasting
#es un conjunto de reglas para aplicar a funciones binarias (suma, resta, multiplicacion, etc) en matrices de diferentes tamaños. 


#Para matrices del mismo tamaño las operaciones binarias son realizadas elemento por elemento.

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b

#Broadcasting permite el tipo de operaciones binarias por matrices de diferentes tamaños
#Se pueden agregar facilmente un escalar 

a + 5 #Podemos pensar en esto como una operacion que ajusta el valor de 5 en una matriz d [5, 5, 5] 

#Se puede hacer esto mismo con matrices de diferentes dimensiones 

M = np.ones((3,3))

M + a

a = np.arange(3)
b = np.arange(3)[:,np.newaxis]

a + b
#El broadcasting ajusta la dimension del producto de la operacion entre las dos matrices
#Reglas de broadcasting
#Ver las reglas del broadcasting pagina 65

#Regla 1: si dos arreglos difieren en su dimension, la forma del que tiene una dimension menor is padded con unos a su lado izquierdo  

#Regla 2: si la forma de los dos arreglos no concuerdan en ninguna dimension, el arreglo con forma igual a uno en esa dimension es acomodado para coincidir con la otra forma. 

#Regla 3: Si ninguna dimension los tamaños no coinciden y ninguno es igual a 1, entonces dara un error. 

#Broadcasting
#Agregar una matriz de dos dimensiones a una de una dimension.
M = np.ones((2, 3))
a = np.arange(3)
#Las formas de las matrices son 
M.shape()
a.shape()
#Por la regla 1, el arreglo (a) tiene menos dimensiones, por lo tanto se rellenan a la izquierda con unos. 

#Ejemplo de broadcasting página 68
#Un ejemplo comun es centrrar una matriz de datos
#Imagina que tienes una matriz de 10 observaciones, cada uno tiene 3 valores. 

X = np.random.random((10, 3))

#Podemos calcular la media para cada caracteristica a lo largo de la primera dimension 

Xmean = X.mean(0)
Xmean

#Ahora podemos centrar la matriz X restandole la media esto con la operacion broadcasting

X_centered = X - Xmean
X_centered

X_centered.mean(0)


#Dibujando una funcion de dos dimensiones
#Un lugar donde el broadcasting es muy util es desplegando imagenes basadas en funciones de dos dimensiones. 
#Si queremso definir la funcion z = f(x,y), broadcasting puede ser usado para calcular la funcion a lo largo del grid

# x, y tienen tienen 50 pasos desde 0 a 5 
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x)**10 +np.cos(10 + y * x)* np.cos(x)

import matplotlib.pyplot as plt

plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar();
plt.show()


#Comparaciones, Mascaras, y logica boleana
#Masking se utiliza cuando se quiere extraer, modificar, contar o manipular de alguna manera valores en las matrices basados en algun criterio, por ejemplo abajo de algun valor o mayor a algun valor.

#Operadores de comparacion como ufuncs

#Numpy tambien implementa operadores comparadores como < > elemento por elemento, el resultado de la comparasion es boleano

x = np.array([1, 2, 3, 4, 5, 6])
x < 3 #Menor que 
x > 3 #Mayor que 
x <= 3 #Menor o igual que 
x >= 3 #Mayor o igual que 
x != 3 #Diferente que  
x == 3 #igual que 

#Tambien es posible hacer una comparasion de elemento por elemento entre dos matrices

(2*x) == (x**2)

#Como en le caso de los operadores aritmeticos, los operadores de comparasion son implementados
# como ufuncs de Numpy, cuando se utiliza x < 3, internamente numpy usa np.less(x,3)

#Los operadores de comparasion en Numpy son :
'''
== np.equal 
!= np.not_equal 
<  np.less
<= np.less_equal
>  np.greater
>= np.greater_equal
'''

#Estas fucionan tambien en matrices de diferentes dimensiones y tamaños 

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))

x < 6

#Trabajando con arreglos boleanos 

#Para contar el numero de elementos verdaderos en un arreglo boleano  
 np.count_nonzero(x < 6)

#Tambien se puede hacer esto mismo con np.sum() el beneficio de hacerlo son esto es que se puede hacer a lo largo de columnas o filas, Falso es interpretado como 0 y True como 1 

np.sum(x< 6, axis=1) #Esto muestra la cantidad de valores menor a 6 en cada columna de la matriz 
 

#Operadores boleanos 

#Los operadores boleanos son and(&), or(|), xor(^) y not(~)
#Estos operadores los podemos utilizar cuando queremos encontrar valores dentro de un rango 
#Para estos operadores es importante utilizar bien los parentesis 
#Los operadores boleanos son los siguientes con sus equivalentes ufuncs

 '''
 &  np.bitwise_and
 |  np.bitwise_or
 ^  np.bitwise_xor
 ~  np.bitwise_not
 '''
#np.sum(inches > 5) & (inches <1)
#Arreglos boleanos como mascaras
#Un patron mas poderoso es usar arreglos boleanos como mascaras, para seleccionar subconjuntos de datos.
#Supongamos que queremos un arreglo de los valores que son menor que algun valor.

x
x < 5 #Con esto se obtiene un arreglo que muestra los valores que cumplen

#Para obtener los elementos del arreglo que cumplen con la condicion se utiliza 
x[x < 5]


#Diferencia entre usar palabras u operadores
#Al utilizar (and), (or) este da el resultado del objeto entero como una unica entidad boleana
#Al utilizar (&), (|) este da el resultado de cada elemento dentro de cada objeto

#Al utilizar and o or es equivalente a preguntarle a Python para tratar al objeto como una unica enitdad boleana. Todos los enteros no iguales a 0 son evaluados como True.

bool(42), bool(0)

bool(42 and 0)

bool(42 or 0)


#Cuando se usa & y | en enteros, la expresion opera en los bits del elemento, aplicando la operacion and o or, en los bits indivudualtes 

bin(42)

bin(49)

bin(42 & 59)

bin(42 | 59)


#Cuando se tiene una matriz de valores boleanos en Numpy, si se utiliza | se operan los valores individuales de las matrices, si se utilzia or, Python toma todo el arreglo como un unico elemento y salta un error 

A = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
B = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
A | B
A or B

#Indexado elegante  

rand = np.random.RandomState(42)

x = rand.randint(100, size=10)

#Supongamos que queremos acceder a tres dinstintos elementos del arreglo anterior
[x[2], x[4], x[5]]

#Otra manera de hacerlo es crear una lista y pasarla como indice

ind = [2, 4, 5]
x[ind]

#Con el indexado elegante, la forma del resultado refleja la forma de las matrices de los indices en lugar de la forma de la matriz que se indexa:

ind = np.array([[3, 7],
               [4, 5]])

x[ind]

#Indexado elegante tambien funciona en multiples dimensiones 
X = np.arange(12).reshape((3, 4))
X

row = np.array([0,1,2])
col = np.array([2,1,3])
X[row,col] #Esto nos da los elementos (0,2), (1,1) y (2,3), estos pares de indices siguen las reglas de broadcasting

#Si se conbiman un vector columan y un vector fila dentro de los indices, obtenemos un resultado de dos dimensiones

X[row[:, np.newaxis], col]

#Es importante recordar que con indexado elegante regresa el valor de la forma de broadcastint de los indices, en vez de la forma del arreglo que es indexado


#Indexado combinado 
#Para operaciones incluso mas poderosas, el indexado elegante se puede combinar con otros esquemas de indexado

#Podemos combinar el indexado elegante con indices simples

X[2, [2, 0, 1]]

#Tambien se puede combinar el indexado elegante con slicing

X[1:, [2, 0, 1]]


#Tambien se puede combinar indexado elegante con masking 

mask = np.array([1, 0, 1, 0], dtype=bool)
X[row[:, np.newaxis], mask]

#Todas estas opciones permiten una manera flexible de accesar y modificar valores de los arreglos

mean = [0, 0]
cov = [[1, 2],
       [2,5]]
X = rand.multivariate_normal(mean, cov, 100)
X.shape
#Ejemplo seleccionar puntos aleatorios pagina 99
%matplotlib inline
import matplotlib.pyplot as plt 
import seaborn; seaborn.set() # for plot styling

plt.scatter(X[:, 0], X[:, 1])
plt.show()

#Modificando valores con indexado elegante 
#El indexado elegante se puede utilizr para acceder a partes de una matriz, esto tambien puede usarse para modificar partes de una matriz. 

x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99 
print(x)

x[i] -= 10

x = np.zeros(10)

#Example Binning Data

#02.08 Sorting 
#Hay que tomar en cuenta los algoritmos de ordenamiento, ya que algunos dependiendo del diseño
#Se pueden tardar mucho tiempo en ordenar el arreglo, tambien depende de si el arreglo es largo
