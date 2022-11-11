class Animal:
    def __init__(self) -> None:
        pass
    def comer(self):
        print('Animal comiendo')

#En Python se soporta la herencia múltiple. varias clases separadas por comas
class Perro(Animal): #La clase hija Perro, hereda de la clase padre Animal
    def __init__(self,nombre) -> None:
         self.nombre=nombre
    def vacunar(self):
        print('El perro se vacuna cada 6 meses')
    def comer(self):
        print('Perro comiendo')
    def saltar(self,que=None): #SImula la sobrecarga de POO
        if que is None:
            print(f'animal saltando')
        else:
            print(f'perro saltando {que}')


class Gato(Animal):
    def __init__(self,nombre) -> None:
        self.nombre=nombre
    def vacunar(self):
        print('El gato se vacuna cada 3 meses')
    #Sobreescritura / override en JAVA


#Crear perro y gato. instanciar
perro:Perro=Perro('Perro Juan')
perro.comer()
perro.saltar('')
perro1:Perro=Perro('Devoramandíbulas')
gato:Gato=Gato('Gato Carlos')

#mostrar por consola
print(perro.nombre)
print(gato.nombre)
print(perro1.nombre)
print(perro.comer)
print(perro.saltar)

#array de perros y gatos
ciudades=['madrid','sevilla','valencia']
#iterar, recorrer lista []
for ciudad in ciudades:
    print(ciudad)

animales=[perro,gato,perro1]
for animal in animales:
    print(animal.nombre)
    animal.vacunar() #polimorfismo