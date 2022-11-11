#https://ellibrodepython.com/programacion-orientada-a-objetos-python
#POO Python

class Prueba: #definir una clase
    nombre='Juan' #atributo de clase

    def __init__(self) -> None: #constructor
        pass
    def saludar(self): #método de instancia. Porque tiene la palabra self
        print(self.nombre) #acceso a atributo del objeto. Llama al atributo de la INSTANCIA (Marta)

    @classmethod #Decorador
    def metodoClase(cls):
        print(f'esto es un método de clase {cls}')
        print(cls.nombre) #gestiona atributos, metodos de la clase. Llama al atributo de la CLASE (Juan)

    @staticmethod #Decorador
    def metodoEstatico():
        print('esto es un método estático')
        #no puede gestionar ni la instnacia ni la clase

#utilizar una clase: instanciar un objeto
prueba1=Prueba() #llama al constructor
prueba1.nombre='marta'
prueba1.saludar() #marta
prueba1.metodoClase()
prueba1.metodoEstatico()