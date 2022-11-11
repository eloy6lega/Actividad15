#EJERCICIO
#crea una clase llamada Alumno
#el alumno tiene nombre, curso, y fecha de matricula
#esos atributos lo pones con un constructor
#damos de alta a los siguientes alumnos
# Juan López, DAM1, 10-01-2023
# María Pérez, DAW1, 15-01-2023
#crea un método (de instancia) para mostrar el detalle de cada alumno
#crea un método que muestre la fecha de hoy

from datetime import date


class Alumno:
    def __init__(self,nombre,curso,fecha) -> None:
        self.nombre=nombre
        self.curso=curso
        self.fechaM=fecha
    def infoAlumno(self): #Método de instancia
        print(f'El alumn@ {self.nombre} asiste a {self.curso} con fecha en {self.fechaM}')
    
    @staticmethod
    def fecha_de_hoy():
        hoy=date.today()
        print(f'Hoy es {hoy}') #Como me pide la fecha mi gusto decide hacer solo la fecha, pero tambien de puede poner con la hora, minutos y segundos con datetime.now()
        

alumno1=Alumno('Juan López', 'DAM1', '10-01-2023')
alumno2=Alumno('María Pérez', 'DAW1', '15-01-2023')
alumno1.infoAlumno()
alumno2.infoAlumno()
alumno1.fecha_de_hoy()
alumno2.fecha_de_hoy()


#POO Python
#Herencia. Herencia múltiple. Sobreescritura. Constructor super
class Padre: #clase Base, Padre, SuperClase
    color='red'
    def __init__(self,categoria) -> None:
        self.categoria=categoria

    @staticmethod
    def consultar():
        print('resultado de clase Padre')

class General:
    color='blue'

#Python soporta la herencia múltiple en orden de las comas
class Hija(Padre,General): #clase Derivada, Hija, Subclase
    unidades=20
    def __init__(self,precio,categoria) -> None:
        super().__init__(categoria) #sin puntos.
        self.precio=precio

    @staticmethod        
    def consultar():
        print(f'Consultando desde la hija')

hija1=Hija(19.95,'oficial') #instanciar la clase
print(f'El total es {hija1.unidades*hija1.precio}')
print(f'El color elegido es: {hija1.color}') #usar atributos de clase Base
hija1.consultar() #Usar métodos de clase Base


#POO Python. Implementación de interfaces
class BuenosHabitos: #esto es una interface
    def comer(): #sin implementar
        pass #el método está sin implementar
    def dormir():
        pass
    def estudiar():
        pass

#Al implementar una interfaz, en Python NO error si te falta algún método
class Deportista(BuenosHabitos): #implementas la interfaz BuenosHabitos
    @staticmethod
    def comer(): #método implemntado
        print('Deportista: come pasta')
    @staticmethod
    def dormir():
        print('Deportista: duerme 8h y siesta')
    @staticmethod
    def estudiar():
        print('Deportista: no estudia')

class Estudiante(BuenosHabitos):
    @staticmethod
    def comer():
        print('Estudiante: come pescado')
    @staticmethod
    def dormir():
        print('Estudiante: duerme 7h, sin siesta')
    @staticmethod
    def estudiar():
        print('Estudiante: estudia 8h o más')

deportista1=Deportista()
deportista1.comer()
deportista1.dormir()
deportista1.estudiar()

estudiante1=Estudiante()
estudiante1.comer()
estudiante1.dormir()
estudiante1.estudiar()


#POO Python. Encapsulamiento
#https://ellibrodepython.com/encapsulamiento-poo

class Cliente:
    __descuento=True #atributo privado por el doble __
    def __init__(self,nombre) -> None: #constructor
        self.nombre=nombre
    def __saludar(self): #método private
        print(f'Hola {self.nombre}')
    def despedir(self):
        print(f'Adiós {self.nombre}')

cliente1=Cliente('Juan López') #instanciar
#cliente1.__saludar  Da error porque es privado :)
#los atributos y métodos privados sólo se pueden utilizar dentro de la misma clase