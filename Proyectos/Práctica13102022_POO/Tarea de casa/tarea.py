#EJERCICIO
#Crea una clase llamada Producto
#esta clase tiene las propiedades:
#nombre, unidades y precio
#En esta clase explica cómo utilizas un constructor, getter/setters y crea un método llamado calcular que muestra unidades * precio * 1.21 de iva
#instancia la clase y crea un objeto.
#muestra por consola, los datos de dicho producto y comprueba que funciona el método calcular.

from math import prod


class producto:

    def __init__(self): #constructor
        self._total = 0

    @property #equivalente a getter:
    def total(self):
        return self._total
    
    @total.setter #Setter. Permite asignarle valor al atributo total
    def total(self, valor):
        if valor < 59.99*3*1.21:
            print('Hemos tenido un error, disculpe las molestias, se lo volveremos a calcular')
        else:
            self._total = valor
        
    @total.deleter
    def total(self):
        del self._total #la palabra 'del', viene de 'delete', lo que hace es borrar.

def main():
    nombre = 'Chaqueta L.A. Lakers'
    unidades = 3
    precio = 59.99
    iva = 1.21

    print(f'El precio total de la compra es {unidades*precio*iva}€') #Hago que por consola muestre el precio de 3 chaquetas con el 1.21iva

print(main()) #Muestra la función main


#Me he ayudado de un vídeo de YouTube y de la página web de Python.org. Consigo que me de el precio de las 3 Chauquetas