from datetime import date, datetime


class ClienteNuevo:
    def __init__(self,f) -> None: #constructor
        self.facturacion=f
    def calcularTotal(self): #método de clase
        print('Calculando el total...')

clientenuevo1=ClienteNuevo(30000) #instanciar un objeto
clientenuevo1.calcularTotal()
clientenuevo1.facturacion=40000 #setter
print(clientenuevo1.facturacion) #40000 getter

#EJERCICIO
#crea una clase llamada Producto
#los productos tendrán nombre, unidades y precio
#crea el siguiente producto: camisa, 20, 9.95
#muestra por pantalla el detalle del prodcuto

class Producto:
    def __init__(self,nombre,unidades,precio) -> None:
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio
    def verDetalle(self):
        print(f'El producto es: {self.nombre} - {self.unidades} - {self.precio}€')
    def consultarPrecio(self):
        if(self.unidades>50):
            self.precio=self.precio*0.9
        print(f'El precio final es {self.precio}€')

producto1=Producto('camisa',20,9.95)
producto1.verDetalle()
producto1.consultarPrecio()


#crea un método en la clase Producto llamado consultarPrecio
#si las unidades son +50, el precio final tiene un 10% de descuento
#da de alta el producto: sombrero, 40, 14.99
#da de alta el producto: chauqeta, 60, 24.99
#muestra el detalle de los productos
producto2=Producto('sombrero',40,14.99) #esto es instanciar
producto3=Producto('chaquetas',60,24.99) #esto es instanciar
producto2.verDetalle()
producto2.consultarPrecio()
producto3.verDetalle()
producto3.consultarPrecio()


#crea una clase para gestionar Empleados
#damos de alta al empleado: Luis López, 25000 euros de salario bruto
#administrativo
#muestra por consola, el detalle del empleado

class Empleados:
    def __init__(self,nombre,salario,cargo) -> None:
        self.nombre=nombre
        self.salario=salario
        self.cargo=cargo
    def detalleEmpleado(self):
        print(f'{self.nombre} - {self.salario}€ brutos anuales - Trabaja en: {self.cargo}')
    def calcularSalario(self):
        print(f'El salario final de {self.nombre} es {self.salario*0.85}€ anuales ')


empleado1=Empleados('Luis López',25000,'administrativo')
empleado1.detalleEmpleado()
empleado1.calcularSalario()

#Contratamos a otro empleado: Laura Sámchez, 32.000
#su puesto jefe de proyecto
#el salario final será el salario bruto - 15%
#muestra por pantalla el salario final de ambos trabajadores
empleado2=Empleados('Laura Sánchez',32000,'jefa de proyecto')
empleado2.detalleEmpleado()
empleado2.calcularSalario()


#crea una clase llamada Alumno
#Datos del alumno: nombre, fechaMatricula, notamedia
#crea un método para mostrar la nota siguiendo estos criterios:
#superior a 5 hasta 7 la nota es Aprobado
#superior a 7 hasta 9 la nota es Notable
#superior a 9 hasta 10 es Sobresaliente
#inferior a 5 es Suspenso
#crea un método para consultar los días que lleva matriculado

class Alumno:
    def __init__(self,nombre,fecha,nota) -> None:
        self.nombre=nombre
        self.fechaMatricula=fecha
        self.notamedia=nota
    def consultarNota(self):
        if(self.notamedia<5):
            print(f'La nota es Suspenso')
        elif(self.notamedia>=5 and self.notamedia<7):
            print(f'La nota es Aprobado')
        elif(self.notamedia>=7 and self.notamedia<9):
            print(f'La nota es Notable')
        else:
            print(f'La nota es Sobresaliente')
    def diasMatricula(self):
        hoy=datetime.today()
        print(f'Hoy es {hoy}')
        fechaFin=datetime.strptime(self.fechaMatricula,"%d-%m-%Y")
        print(fechaFin)
        dias=hoy-fechaFin
        print(f'Dias matriculado: {dias}')

alumno1=Alumno('Carlos Alcaraz','20-12-2020',8.2)
alumno1.consultarNota()
alumno1.diasMatricula()


#crea una clase llamada Calculo con dos propiedades n1 y n2
#crea un objeto con n1=15 y n2=7
#crea un método llamado sumar que muestra la suma de los dos números

class Calculo:
    def __init__(self,n1,n2) -> None:
        self.n1=n1
        self.n2=n2
    def suma(self):
        print(f'La suma de n1 = {self.n1} y n2 = {self.n1+self.n2}')

operacion1=Calculo(15,7)
operacion1.suma()

