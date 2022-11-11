#te pide cuántos números quieren probar
numeros=int(input('cuántos números quieres probar'))
#recorre todos los números
for numero in range(numeros):
    print(f'el número es {numero}')
    if(numero==11 or numero==15):
        print('es un número especial')
#cuando aparezca cada número lo escribes por pantalla
#pero los números 11 y 15 muestras un mensaje diciendo que son 
#números especiales

