class Cliente:
    def __init__(self) -> None:
        self.nombre=input('Dime el nombre del cliente: ')
        self.ciudad=input('Dime la ciudad del cliente: ')
        self.facturacion=input('Dime la facturación del cliente: ')


    def confirmarRegistro(self):
        print(f'Se ha guardado {self.nombre}.')

cliente1=Cliente() #INSERT INTO CLIENTES VALUES.....
#cliente1.confirmarRegistro() LO COMENTO PARA RECORRER UNA LISTA.

#se podría dar de alta a más clientes
cliente2=Cliente()

cliente3=Cliente()

#donde pijos se guardan los datos?
#solución: se guardan en el programa, en la memoria de tu equipo

#clientes habituales : tabla de clientes
clienteHab=[cliente1,cliente2,cliente3]

#select * from clientes
for cliente in clienteHab:
    cliente.confirmarRegistro()