print('____________________________________________________________________________________________________')

class Trabajador:
    def __init__(self) -> None:
        self.nombre=input('Dime el nombre del trabajador: ')
        self.num_seg_soc=input('Dime su número de la seguridad social: ')
        self.ciudad=input('Dime su ciudad de residencia: ')


    def mostrar_Ficha(self):
        print(f'La ficha de {self.nombre} es: Sr./Sra. {self.nombre} - con {self.num_seg_soc} número en la seguriadad social - de la ciudad de {self.ciudad}')

    def calcularNeto(self):
        self.bruto=float(input('Dígame su salario bruto: '))
        self.pagas=float(input('¿Número de pagas? (12 o 14): '))
        neto=(self.bruto*0.8)/self.pagas
        print(f'El/la trabajador/a {self.nombre} tendrá un salario neto de {round(neto,2)}€.')

trabajador1=Trabajador()
trabajador1.calcularNeto()


#TU EQUIPO DE TRABAJO TENDRÁ 4 TRABAJADORES. Dalos de alta y muestra su nombre y su num_seg_soc

trabajador2=Trabajador()

trabajador3=Trabajador()

trabajador4=Trabajador()

datosTrab=[trabajador1,trabajador2,trabajador3,trabajador4]

trabajadores=map(lambda x: x.mostrar_Ficha(),datosTrab)
print(list(trabajadores))

#nuestra aplicación va a tener una funcionalidad para que el
#trabajador pueda calcular su salario.
#Le vamos a pedir sólamente el salario bruto y el número de pagas  
#con eso le mostramos el salario neto mensual.
#el cálculo (me lo invento) sería : bruto-20% bruto / 12 o 14 pagas

print('____________________________________________________________________________________________________')
