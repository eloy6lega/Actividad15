#Ejercicio 1
#Crea una función que pide dos argumentos numéricos
#La división de esos dos números que has metido por consola
#Resultado redondeado a dos dígitos (rouns())
#la función se llama ejercicio1

#Ejercicio 2
#Tenemos la siguiente cadena
#madrid,sevilla,valencia,córdoba,jaén
#necesitamos "dividir" esta cadena por ciudades (split())
#el separador es, obviamente la coma
#muestra por consola las ciudades una a una (for....in....)

#Ejercicio 3
#Leer datos de un archivo. Explicación
#(ESTÁ EN SOLUCIONES YA!!!)

#Ejercicio 4
#Muestra una pregunta por consola. El usuario escribe la respuesta.
#La respuesta se guarda en el archivo de texto
#esperamos a tener todas las respuestas y las enviamos juntas
#with open('archivo','w') as f:
def ejercicio4():
    from datetime import datetime

    print('Dime la capital de chipre')
    respuesta=input('La respuesta es: ')
    hoy=datetime.now()
    hoyf=hoy.strftime('%d-%m-%Y %H:%M:%S')
    with open('datos2.txt','a') as f:
        f.write(f'Respuesta: {respuesta} \n Hora: {hoyf}')

ejercicio4()
#guardar la respuesta en un archivo + fecha y hora actuales
#no se envío otra respuesta, NO romàs la anterior
