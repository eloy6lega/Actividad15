print('___________________________________________________________________________________________________________________________________________________________')
print(' ')
primos:int=int(input('Dime cuantos números primos quieres: '))
print(f'Quieres ver {primos} números primos')
numero=3 #primer número para comprobar
for numero in range(primos):
    esprimo=True
    #comprobar si es o no primo
    if numero%2==0 or numero%3==0 or numero%5==0:
        esprimo=False
    if esprimo:
        print(f'El número es primo: {numero}')