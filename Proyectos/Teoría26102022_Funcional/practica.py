#Ejercicio1
#creas una clase en Python para almacenar Productos
#los atributos son nombre, color, unidades, precio
#si quieres utiliza un constructor
#crea un método que permita mostrar el info del producto : nombre, stock unidades

#alta tres productos a tu gusto.


from operator import add
from functools import reduce
import statistics


class Productos: #clases
    def __init__(self,nombre,color,unidades,precio) -> None: #constructor
        self.nombre=nombre
        self.color=color
        self.unidades=unidades
        self.precio=precio
    def informacionProductos(self): #método para que me de la info
        print(f'Información del producto: {self.nombre} - {self.unidades} unidades - {self.precio}€')
    def getUnidades(self):
        return self.unidades
    def getImporte(self):
        return self.unidades*self.precio
    def getImporteConIVA(self):
        return self.unidades*self.precio*1.21
        

p1=Productos('Balón de Baloncesto', 'Rojo Molten', 100, 24.99)
p2=Productos('Mallas deportivas Cortas', 'Negras o Blancas', 200, 7.99)
p3=Productos('Zapatillas LeBron Witness 6', 'Amarillo pastel', 50, 120.00)

cesta=[p1,p2,p3]

for p in cesta:
    p.informacionProductos()



#Ejercicio 2
#creas 5 productos - list
#total de uds
#total de importe
#total de factura con 21% iva incluido

p4=Productos('Camiseta térmica', 'Blaco, Negro, Azul', 200, 11.99)
p5=Productos('Calcetines Nike Sport', 'White', 500, 6.99)
p6=Productos('Protector de rodilla', 'Negra', 150, 6.99)
p7=Productos('Cinta para pelo basketball', 'Blanca, Negra, Azul', 500, 4.99)
p8=Productos('Cindactalia', 'Blanca', 300, 3.99)

lalista=[p4,p5,p6,p7,p8]

totalUnidades=map(lambda p:p.getUnidades(),lalista)
sumaTotalUnidades=reduce(add,list(map(lambda p:p.getUnidades(),lalista)))
print(list(totalUnidades))
print(sumaTotalUnidades)

sumaTotal=reduce(add,list(map(lambda p:p.getImporte(),lalista)))
print(f'El importe final de la factura es: {sumaTotal} sin IVA incluido')

sumaTotalConIVA=reduce(add,list(map(lambda p:p.getImporteConIVA(),lalista)))
print(f'El importe final de la factura es: {sumaTotalConIVA} IVA incluido')