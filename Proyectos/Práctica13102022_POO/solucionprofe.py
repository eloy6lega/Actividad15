#SOLUCIÓN EJERCICIO
#Crea una clase llamada Producto
#esta clase tiene las propiedades: nombre, unidades y precio
#En esta clase explica cómo utilizas un constructor, getter/setters y crea un método llamado calcular que muestra unidades * precio * 1.21 de iva
#instancia la clase y crea un objeto.
#muestra por consola, los datos de dicho producto y comprueba que funciona el método calcular.

from datetime import date, timedelta


class Producto:
    #constructor en python
    def __init__(self,nombre,unidades,precio) -> None:
        #esta clase tiene las propiedades: nombre, unidades y precio
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio

    def calcular(self):
        print('Estoy calculando')

#instanciar : crear un objeto en base a la clase
producto=Producto('juan',15,9.99)
#mostrar por consola alguna propiedad (getter)
print(producto.nombre)
producto.calcular()

#TAREA
#Tienes que crear una clase perro. propiedades : nombre, edad. método comer:estoy comiendo
#crear perro lupo de 5 años y comiendo

class Animal:
    patas=4
    def vacunar(self):
        print("vacunado")

#crear una interfaz
class IAcciones:
    def correr(self,velocidad):
        pass
    def dormir(self,horas):
        pass

class Perro(Animal,IAcciones): #herencia + implementar una interface
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
    def comer(self):
        print('El perro come')
    def correr(seslf,velocidad):
        print(f'El perro corre a {velocidad}km/h')
    def vacunar(self):
        print('vacunando')
    def vacunar(self,fecha): #sobreescritura. overload. mismo nombre, diferentes parámetros
        hoy=date.today() #hay que sumar 3 meses o 90 días
        #Para operar con fechas se puede usar el método timedelta()
        vacunacion=hoy+timedelta(days=90)
        print(f'Hoy es {fecha}. La fecha de vacunación es: {vacunacion}')

perro=Perro('Lupo',5)
print(perro.nombre)
print(perro.edad)
print(perro.patas)
perro.comer()
perro.correr(10)
#fecha actual se muestra con el módulo date y la función today
perro.vacunar(date.today())

#       ◥------◥
#       l ● ▄ ◉ l ѠOOƑ!
#       l‿/ʊ\‿l
#       l══o══l
#       ︳ ︳︳ l⊃
#       ఋ︵ ఋ

#           ______________________$$$$
#           _______________$$$$________$$$$$
#           _____________$________________________$$
#           ____________$_____________________________$
#           ___________$__________________________________$
#           ___________$___________________________________$
#           __________$__$______________________$__________$
#           ________$__$___$$_________$$____$__________$$
#           ______$___$__$$__$_____$$__$_$_____________$$
#           ______$___$____$$_________$$___$_______________$
#           ______$___$________________________$_______________$
#           ______$____$_______________________$_____________$
#           ________$__$____$$$_____________$___________$$
#           ________$__$__$______$___________$_________$
#           ________$__$__$______$___________$_______$
#           __________$$____$$$_____________$$____$$
#           __________$$_____________________$__$____$$
#           ___________$_$$$$$$_____$$______$$_$
#           _____________$___$______$$$_______________$
#           _____________$_____$$$$____________________$
#           _____________$________________________________$
#           ____________$_________________________________$
#           ____________$_________________________________$
#           ____________$___________________________________$
#           ____________$___________________________________$
#           __________$_________________________$___________$
#           __________$__________$___________$_____________$
#           ________$__$________$_________$_______________$
#           ______$____$__________$_______$_______________$
#           ______$____$____________$___$_________________$
#           ____$______$_____________$_$_______$_________$
#           ____$______$________$____$$________$_________$
#           ____$______$________$____$$_______$__________$
#           ____$______$________$_______________$__________$
#           ____$______$________$_______________$____________$
#           _$$_______$________$_______________$____________$
#           $___$______$________$$___________$$____________$
#           $___$______$________$__$_______$__$____________$
#           _$$$______$________$____$___$_____$___________$
#           ____$______$________$______$_______$___________$
#           ____$______$________$_____$________$___________$
#           __$________$________$$$$___$$$__$_________$
#           __$________$________$______$$______$$_________$
#           $________$__________$_________$$$__$__________$
#           $______$__________$$$$$$$$______$__________$
#           $_$_$$__________$_____________$$$$__$_________$
#           _$$$$___________$______________________$________$
#           _____$__$__$__$_$______________________$__________$
#           ______$$__$___$__$______________________$____________$
#           _______$___$___$__$________________________$_$__$__$__$
#           _________$$$$$__________________________$_$_$$$$


#TAREA 2
#Clase Gato. propiedades : nombre y color. método comer: el gato come
#crear Gato mizifu de color verde y comiendo

class Gato:
    def __init__(self,nombre,color) -> None:
        self.nombre=nombre
        self.color=color
    def comer(self):
        print('El gato come')

gato=Gato('Mizifu','Verde')
print(gato.nombre)
print(gato.color)
gato.comer()

#       ─────▄█▄█─────────────
#       ────█████▄▄▄──────────
#       ──────███████▄────────
#       ░░░░░░█▀█▀█████░░░░░░░
#       ░░░░░▄█▄█░▄████▄▄▀░░░░

#TAREA 3
#con el método vacunar (Animales) le metes la fecha de hoy
#para perro, vacuna es perro + 3 meses
#para gato, vacuna es gato + 6 meses

#(HECHO ARRIBA EN 'PERRO')



# ╭━━━┳╮╱╱╭━━━┳╮╱╱╭╮
# ┃╭━━┫┃╱╱┃╭━╮┃╰╮╭╯┃
# ┃╰━━┫┃╱╱┃┃╱┃┣╮╰╯╭╯
# ┃╭━━┫┃╱╭┫┃╱┃┃╰╮╭╯
# ┃╰━━┫╰━╯┃╰━╯┃╱┃┃
# ╰━━━┻━━━┻━━━╯╱╰╯