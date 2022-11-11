#condicional
from unittest import result


respuesta=input('Dime la capital de Chipre: ')
if respuesta=='nicosia'or respuesta=='NICOSIA':
    print('¡¡¡MUY BUENA CRACK!!!')
else:
    print('MAS MALO QUE PEGARLE A UN PADRE...')

#bucle for
#numeros=(1,2,3,4,5) #array
numeros=range(1, 6, 2) #es lo mismo que arriba pero más fácil y simplificado
total=0
for n in numeros:
   print(n) #escribirá los numeros del array
   total=total+n #y acumulará los numeros haciendo la suma
print('El total es '+str(total)) #fuera del for, al final me pintará 1+2+3+4+5=15 (valores del array)

#bucle while (indeterminado)
resultado=input('Dime el río más largo de África: ')
intentos=1
while resultado!='nilo': #la expresión != significa condicional con negado. "Si resultado es distinto de nilo, ..."
    print('Vaya malo jaja')
    intentos+=1
    resultado=input('Dime el río más largo de África: ')
#print('Acertaste en el intento número '+str(intentos)+'. Puedes continuar...') #es lo mismo que el de abajo pero este es más largo y mas "fácil"
print(f'Acertaste en el intento número {intentos}. Puedes continuar...') #hay que poner la f al principio y poner la variable en llaves {}

#bucle do while*
#montaña='teide'
contador=0
while True:
    contador+=1
    respuestaPregunta=input(f'{contador} Dime la montaña más alta de España: ')
    if respuestaPregunta.lower()=='teide':
        break
print(f'Has adivinado la montaña en el intento {contador}')