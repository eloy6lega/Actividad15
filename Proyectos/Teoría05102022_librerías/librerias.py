#método de la librería str
from calendar import calendar, isleap
from datetime import date, datetime
import math
from operator import imod
import random
from time import time
from calendar import isleap


texto='en un lugar de la mancha'
cappitulares=texto.capitalize() #Me pone la primera letra de la frase en mayus.
print(cappitulares)
print(texto.index('l')) #le decimeos que carácter queremos buscar y nos dirá en que posición está ('l' estará en la posición 6 (empezamos desde 0 a contar))
palabras=texto.split(' ') #me sapara la frase dentro de unn array por palabras
print(palabras)
aes=texto.count('a') #contará cuantas 'a' tengo en la frase
print(aes)

#librerías numéricas
aleatorio=random.randint(0,100) #me dará un número aleatorio entre los valores que le escriba
print(aleatorio)

#muestra el seno de 1
seno=math.sin(1)
print(seno) #0.8414709848078965

#te doy el radio y muestra el área de un círculo. 2PIr2
radio=20
print(math.pi)
print(math.pi*radio**2) #1256.6370614359173
#te doy un número con decimales y lo redondeas 2.49=2 2.51=3
print(math.ceil(2.44)) #3
print(math.ceil(2.51)) #3
print(round(2.49)) #2
print(round(2.51)) #3

#fechas
#fecha de hoy en formato largo. 05 de octubre de 2022
hoy=datetime.now()
print(hoy)
print(hoy.utcnow())
print(hoy.day)
print(hoy.month)
print(hoy.strftime("%d de %B del %Y - %H:%M:%S"))

#hora actual 09:59:02
print(hoy.strftime("%H:%M:%S"))

#mes actual octubre


#preguntas el año
#me respondes si ese año fue o no bisiesto
año=int(input('Dime que año quieres comprobar: '))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print('El año era, es o será bisiesto')
else:
    print('el año NO es bisiesto')

#print('Muy bien, ahora lo vamos a hacer con otro comando')
#from calendar import isleap
#año=int(input('Dime otro año: '))
#print()

#if calendar.isleap(año):
 #   print('El año es bisiesto')
#else:
#    print('El año NO es bisiesto')

#conversión de números
#pides un número decimal: 192
#muestras el número binario

print(bin(192))