#UTILIZO PARTE DEL CÓDIGO DE AYER PARA METER LA VARIANTE DEL EJERCICIO
#TAREA
# perros y gatos : perro ladra, gato maúlla
# método hablar()

# collection de perros y gatos
# itera la collection y que cada uno hable
# llaman todos al método hablar, pero los perros ladran y los gatos maúllan (así debe salir por consola)
# hablar que se comporta diferente en función del objeto : POLIMORFISMO
from datetime import date,timedelta

class Animal:
    patas=4
    def hablar(self,ladrar,maullar):
        print("está... ")

#crear una interfaz
class IAcciones:
    def hablar1(self,ladrar):
        pass
    def hablar2(self,maullar):
        pass

class Perro(Animal,IAcciones): #herencia + implementar una interface
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
    def ladrar(self):
        print('El perro ladra')
    def correr(seslf,velocidad):
        print(f'El perro corre a {velocidad}km/h')
    def vacunar(self):
        print('vacunando')
    def vacunar(self,fecha): #sobreescritura. overload. mismo nombre, diferentes parámetros
        hoy=date.today() #hay que sumar 3 meses o 90 días
        #Para operar con fechas se puede usar el método timedelta()
        vacunacion=hoy+timedelta(days=90)
        print(f'Hoy es {fecha}. La fecha de vacunación es: {vacunacion}')
    def hablar1(self,ladrar):
        print('Estoy ladrando')

perro=Perro('Lupo',5)
print(perro.nombre)
print(perro.edad)
print(perro.patas)
perro.ladrar()
perro.correr(10)
#fecha actual se muestra con el módulo date y la función today
perro.vacunar(date.today())
perro.ladrar()


class Gato:
    def __init__(self,nombre,color) -> None:
        self.nombre=nombre
        self.color=color
    def maullar(self):
        print('El gato maulla')
    def hablar2(self,maullar):
        print('Estoy maullando')

gato=Gato('Mizifu','Verde')
print(gato.nombre)
print(gato.color)
gato.maullar()



# ╭━━━┳╮╱╱╭━━━┳╮╱╱╭╮
# ┃╭━━┫┃╱╱┃╭━╮┃╰╮╭╯┃
# ┃╰━━┫┃╱╱┃┃╱┃┣╮╰╯╭╯
# ┃╭━━┫┃╱╭┫┃╱┃┃╰╮╭╯
# ┃╰━━┫╰━╯┃╰━╯┃╱┃┃
# ╰━━━┻━━━┻━━━╯╱╰╯