#Crear una clase llamada Operaciones
#El método sumar me permite sumar dos números o tres
#crea un objeto de operaciones y prueba los dos métodos

from ipaddress import summarize_address_range


class Operaciones:
    def __init__(self) -> None:
        pass
    def sumar(self,a,b,c=None): #Sobrecaarga
        if c is None:
            return a+b
        else:
            return a+b+c

operacion=Operaciones()
resultado1=operacion.sumar(4,5)
print(resultado1)
resultado2=operacion.sumar(1,4,6)
print(resultado2)

#no es necesario clases
#por consola pides la fecha del examen
#introduces la fecha correcta... que es 14/12/2022
#te muestran los días que faltan

from datetime import datetime

def dias_restantes():
    fecha=input('Dime la fecha del examen: ')
    dia_examen=datetime.strptime(fecha,'%d-%m-%Y')
    hoy=datetime.now()
    dias=dia_examen-hoy
    print(dias)
dias_restantes()