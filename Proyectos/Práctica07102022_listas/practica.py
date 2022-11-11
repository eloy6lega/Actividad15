#Crea una lista llamada elementos
#introduce los siguientes valores 
#1 - "madrid" - True - 19.95

elementos=[1,"madrid",True,19.92,1] #por defecto es una list
# corchetes [] es una lista. soporta duplicados y ordered
print(elementos)

#¿es posible introducir de diferentes tipos de datos?
#sí es posible

#Muestra por consola, el segundo elemento. Debe salir madrid
print(elementos[1])
#Muestra por consola, el último elemento. Debe salir 19.95
print(elementos[-1])

#declarar función para reutilizarla
def mostrar():
    for elemento in elementos:
        print(f'el elemento {elemento} su valor es {elemento}')


#Muestra por consola todos los elementos con la frase
#el elemento x es tal
#recorrer una lista
mostrar()

 #Añade sevilla
elementos.append("sevilla") #coloca al final

#dónde se añade?
mostrar()
#Vuelve a mostrar la lista por consola. Usando funciones.#
