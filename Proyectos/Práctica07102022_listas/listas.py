#Actividad 4 : Python librerías.

#Crea un proyecto nuevo llamado practica07102022_listas.
#Crea un archivo llamado listas.py

#Crea una lista llamada elementos
#introduce los siguientes valores 
#1 - "madrid" - True - 19.95
elementos=(1, 'madrid', True, 19.95)
#¿es posible introducir diferentes tipos de datos? SI
#Muestra por consola, el segundo elemento. Debe salir madrid
print(elementos[1])
 #Muestra por consola, el último elemento. Debe salir 19.95
print(elementos[-1])

#declarar función para reutilizarla
def mostrar():
    for elemento in elementos:
        print(f'El elemento {elementos} su valor es {elementos}')
#Muestra por consola todos los elementos con la frase
#el elemento x es tal
#recorrer una lista


#Añade sevilla
#dónde se añade?
#Vuelve a mostrar la lista por consola. Usando funciones.
