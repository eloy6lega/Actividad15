#Polimorfismo - POO Python
#https://www.cosmiclearn.com/lang-es/python-polymorphism.php
#https://ellibrodepython.com/polimorfismo-en-programacion

#POO características. herencia / encapsulamiento / abstracción
#sobreescritura override
#sobrecarga overload
#mismo método con diferentes parámetros
#sumar(n1,n2)
#sumar(n1,n2,n3)
#en Python, toma el último método: Python soporta argumentos opcionales
#sumar(n1,n2,n3=0)

#Polimorfismo con anulación de métodos y crear lista de animales

from types import CoroutineType
from unicodedata import name


class Animal(): #clase base
    @staticmethod
    def comer():
        print('un animal come')

class Perro(Animal):
    @staticmethod
    def comer(): #anulación de método
        print('El PERRO come pienso para perros')

class Gato(Animal):
    @staticmethod
    def comer():
        print('El GATO come pienso para gatos')
perro=Perro()
gato=Gato()

perro1=Perro()
perro2=Perro()
perro3=Perro()
perro4=Perro()
gato1=Gato()
gato2=Gato()
gato3=Gato()

animales=[gato1,perro2,gato2,perro3,gato3] #lista
for animal in animales:
    print(animales)
    animal.comer() #polimorfismo


#EJERCICIO DE HERENCIA
#tienes Estudiante, Deportista y Actor son tres clases con su constructor
#cada clase, pide nombre y ciudad
#crea un método llamado detalle para informar sobre nombre y ciudad
#da de alta a un esstudiante, un deportista y un actor

class Personas():
    def __init__(self,nombre,ciudad) -> None:
        self.nombre=nombre
        self.ciudad=ciudad
    def detalle(self):
        print(f'{self.nombre} es de {self.ciudad}')

class Estudiante(Personas):
    pass

class Deportista(Personas):
    pass

class Actor(Personas):
    pass

estudiante=Estudiante('Rodrigo Fernández','Madrid')
deportista=Deportista('Lorenzo Brown','Albacete')
actor=Actor('Juanjo Pérez','Zaragoza')

estudiante.detalle()
deportista.detalle()
actor.detalle()


#EJERCICIO
#gestionar datos de una fuente de datos
#APIRest, DBRelacional, DBNoRelacional, : implementar la interface
#open, read, create, delete, update, close : metodos interface
#crea una conexión a DBRelacional y uso los métodos open, read, close

class Conexiones(): #interface
    def open(): #sin implementar
        pass #el método está sin implementar
    def read(): #sin implementar
        pass #el método está sin implementar
    def create(): #sin implementar
        pass #el método está sin implementar
    def delete(): #sin implementar
        pass #el método está sin implementar
    def update(): #sin implementar
        pass #el método está sin implementar
    def close(): #sin implementar
        pass #el método está sin implementar

class APIRest(Conexiones):
    @staticmethod
    def open(): #método implementado
        print('Estoy abriendo APIRest')
    @staticmethod
    def read(): #método implementado
        print('Estoy leyendo APIRest')
    @staticmethod
    def close(): #método implementado
        print('Estoy cerrando APIRest')

class DBRelacional(Conexiones):
    @staticmethod
    def open(): #método implementado
        print('Estoy abriendo DBRelacional')
    @staticmethod
    def read(): #método implementado
        print('Estoy leyendo DBRelacional')
    @staticmethod
    def close(): #método implementado
        print('Estoy cerrando DBRelacional')

class DBNoRelacional(Conexiones):
    @staticmethod
    def open(): #método implementado
        print('Estoy abriendo DBNoRelacional')
    @staticmethod
    def read(): #método implementado
        print('Estoy leyendo DBNoRelacional')
    @staticmethod
    def close(): #método implementado
        print('Estoy cerrando DBNoRelacional')

conexionAPI=APIRest()
conexionDBR=DBRelacional()
conexionDBNR=DBNoRelacional()
conexionDBR.open()
conexionDBR.read()
conexionDBR.close()


#EJERCICIO
#crea una clase Figura que tiene la propiedad num_lados
#crea la clase Triangulo, Cuadrado y Pentagono
#todas estas clases heredan de Figura.
#el método info, indica los lados de la figura y cómo se calcula su área
#crea un triángulo y consulta su método info

class Figura():
    def __init__(self,num_Lados) -> None:
        self.num_Lados=num_Lados
    def info(self):
        print(f'tiene {self.num_Lados} lados')

class Triangulo(Figura):
    def info(self):
        print(f'El triángulo tiene {self.num_Lados} lados')
        print('Calculando área: base*altura/2')

class Cuadrado(Figura):
    def info(self):
        print(f'El cuadrado tiene {self.num_Lados} lados')
        print('Calculando área: lado*lado')

class Pentagono(Figura):
    def info(self):
        print(f'El pentágono tiene {self.num_Lados} lados')
        print('Calculando área: (Perímetro x Apotema)/2')

t=Triangulo(3)
t.info()
c=Cuadrado(4)
c.info()
p=Pentagono(5)
p.info()