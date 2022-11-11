from random import randint

#al iniciar el programa se calcula un número aleatorio del 1 al 10
numero_secreto=randint(1,10)
print(numero_secreto)

#pregunta qué número es hasta que lo adivienes
tu_numero=0 #inicializa el número
intentos=0 #acumulador de intentos
while tu_numero!=numero_secreto: #no for porque no sabes cuándo será true
   tu_numero=int(input('adivina el número')) 
   intentos+=1 #acumula los intentos
#muestra el número adivinado y los intentos necesario
print(f'has adivinado el número con {intentos} intentos')


