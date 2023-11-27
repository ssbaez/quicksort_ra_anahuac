import time
import random
import sys

sys.setrecursionlimit(20001)

caso1_range = 500
caso2_range = 1000
caso3_range = 10000
ejecuciones = 100

def quicksort(lista, low, high):
  inicio = time.time()
  if low < high:
    # division y colocacion de pivote
    pi = partition(lista, low, high)
    quicksort(lista, low, pi - 1)
    quicksort(lista, pi + 1, high)
  fin = time.time()
  return fin - inicio
      
 
def partition(lista, low, high):  
  # Pivote, el ult elemento
  pivot = lista[high]
  
  # Apuntador del ult elemento mas peq
  i = low - 1
 
  for j in range(low, high):
    if lista[j] <= pivot:
      # Cambio de apuntador
      i = i + 1
      # Cambio de elementos
      (lista[i], lista[j]) = (lista[j], lista[i])
  
  # Se intercambia al final el pivote
  (lista[i + 1], lista[high]) = (lista[high], lista[i + 1])
  return i + 1

# crea las listas dependiendo el caso
def mkSet(n):
    lista = [0] * n
    if n == caso1_range:
        for i in range(n):
            lista[i] = numRandom(n,0)
    elif n == caso2_range:
        for i in range(n):
            lista[i] = numRandom(n)
    elif n == caso3_range:
        for i in range(n):
            lista[i] = numRandom(n)
    return lista

# devuelve un numero int o float al azar
def numRandom(n,k=None):
    num = random.randint(0,n)
    if num%2 == 0 and k == None:
        return random.randint(0,n)
    else:
        return round(random.uniform(0.5,n),2)

# ejecuta el algoritmo de ordenamiento un numero determinado de ejecuciones
def exec(l):
    tt = 0
    for i in range(ejecuciones):
            t_ejecucion = quicksort(l, 0, len(l)-1)
            tt += t_ejecucion
    return tt

# mensaje de salida una vez que se terminaron todas las ejecuciones
def message(n,rango,tt):
    print('Despues de {} ejecucion(es) de ordenamiento para el caso {} con un conjunto de {} datos, el tiempo promedio fue de:'.format(ejecuciones,n,rango))
    print('{:f}'.format(tt/ejecuciones))

# punto de entrada de los casos
def caso(n):
    if n == 1:
        l = mkSet(caso1_range) 
        tt = exec(l)
        message(n,caso1_range,tt)
    elif n == 2:
        l = mkSet(caso2_range)
        tt = exec(l)
        message(n,caso2_range,tt)
    elif n == 3:
        l = mkSet(caso3_range)
        tt = exec(l)
        message(n,caso3_range,tt)
 
caso(1)
#caso(2)
#caso(3)