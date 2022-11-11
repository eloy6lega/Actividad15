#pregunta cuántos números quieres evaluar
numeros=int(input('dime los números a evaluar'))
primos=[3,5,7]
#bucle para recorrer los números
for numero in range(numeros):
    es_primo=True
    if numero%2==0 or numero%3==0 or numero%5==0 or numero%7==0:
        es_primo=False
    if es_primo:
        primos.append(numero)

print(primos)       

