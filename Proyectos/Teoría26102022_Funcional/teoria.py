#Python con programación funcional
#Características propias del paradigma declarativo
#no vamos a utilizar condicional ni bucles como estructuras
#utilizaremos funciones: filter, map, reduce

#function map:
#tenemos un listado de ventas y quieres calcular el total de la factura con iva incluido (21%)





ventas=[1000,1500,2100,1950.25]
totalFactura=[]

def calcularTotal(x):
    return x*1.21

#imperativo
for venta in ventas:
    totalFactura.append(venta*1.21)
print(totalFactura) #muestra al finalizar

#declarativo. map
totalFactura=map(calcularTotal,ventas) #ciclo bucle dentro
print(f'Programación funcional: {list(totalFactura)}')

#Práctica
#tienes una lista de ciudades
#mostrar las ciudades en mayúsculas

ciudades=['madrid','valencia','fuengirola','albacete','zaragoza']
ciudadesMayus=[]

def CiudMays(x):
    return x.upper()

#1 DECLARATIVA CON MAP
ciudadesmayus=map(CiudMays,ciudades)
print(f'Forma 1 map: {list(ciudadesmayus)}')

#2 IMPERATIVA CON FOR IN
for ciudad in ciudades:
    ciudadesMayus.append(ciudad.upper())
print(ciudadesMayus)

#3 DECLARATIVA CON LAMBDA
ciudadesmayus=map(lambda x: x.upper(),ciudades)
print(list(ciudadesmayus))


#FILTER
numeros=[10,11,15,14,18]
pares=filter(lambda n: n%2==0,numeros)
print(f'Los numeros pares son: {list(pares)}')

#Prácica
#crea una lista de años
años=[1980,1940,1952,1953,1965,1356,1094,1395]
#muestra los bisiestos: funcion en python que devuelve el bisiesto
#importar módulo
#1
from calendar import isleap
import statistics
bisiesto=filter(lambda a:isleap(a),años)
print(f'Con lambda: {list(bisiesto)}')


#REDUCE

from functools import reduce
from importlib import import_module

facturacionClientes=[1500,1800,950,147.8]
sumaTotal=reduce(lambda factura,total:factura+total,facturacionClientes)
print(f'El total de facturaión es {sumaTotal}')

#Práctica
#un alumno tiene las notas de 5 asignaturas
#muestra la suma total de sus notas
#muestra la nota media

NAl=[4.5,7,8,5,9]
sumNot=reduce(lambda notillas,suma:notillas+suma,NAl)
print(f'La suma de las notas del alumno es: {sumNot}')
media=sumNot/len(NAl)
print(f'La media del niño es: {media}')

#VERSION DE ALLAM
from operator import add

notasALLAM=[6,7,8,10,2]
totalnotasALLAM=reduce(add,notasALLAM)
print(f'(ALLAM) La suma total es: {totalnotasALLAM} y la nota media es {statistics.mean(notasALLAM)}')


#Práctica
#Practica
# Por consola te pide un número.
# te lo sigue pidiendo hasta que pulses 9
# cuando ya has acabado te dice:
# cuántos números has introducido
# su suma total 
# y la media
# puedes mezclar imperativa y declarativa.

#VAMOS A HACERLO POR PASOS PARA NO BLOQUEARNOS
#pedir número
#seguir pidiendo números hasta pulsar 9 : bucle
#acumular los numeros en un list (no puede ser set porque los valores se deben poder repetir)
#tengo una lista: declarativa: map, reduce : contador, total, media

# pseudocódigo / diagrama de flujo

#prgrama. Escribir en Python
def los_numeros_de_pepe():
    numerospuestos=[]
    try:
        while True:
            numeropedido=int(input('Dime un número: '))
            if numeropedido==9:
                break
            else:
                numerospuestos.append(numeropedido)

        print(numerospuestos)
        print(f'HAS PUESTO UN TOTAL DE {len(numerospuestos)} NÚMEROS')

        totalPedidos=reduce(add,numerospuestos)

        print(f'La suma de los números que has puesto es {totalPedidos}')
        print(f'La media es: {totalPedidos/len(numerospuestos)}')
    except:
        print('Ha habido un problema, escriba un número válido...')
        los_numeros_de_pepe()

los_numeros_de_pepe()