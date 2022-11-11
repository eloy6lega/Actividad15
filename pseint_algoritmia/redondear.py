#pides un número a tu gusto
from random import randint

numero=int(input('dime un número: '))
#lo divides por un número aleatorio entre 1 y 10
divisor=randint(1,10)
print(divisor)
#si el resto es cero, muestra el cociente tal cual
if(numero%divisor==0): #el resto de la división
    print(f'el cociente es exacto {numero/divisor}')
#si el resto No es cero, muestra el cociente con dos decimales
else:
    print(f'el cociente no es exacto {round(numero/divisor,2)}')
