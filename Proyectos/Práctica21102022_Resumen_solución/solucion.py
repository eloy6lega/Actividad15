#Ejercicio 1
def ejercicio1A():
    def ejercicio1(x,y):
            return round(x/y,2) #ejemplo de método sobrbecargado

    numero1=int(input('Dime el primer número: '))
    numero2=int(input('Dime el segundo número: '))
    resultado=ejercicio1(numero1,numero2)
    print(resultado)

#ejercicio1A()

#Ejercicio 2
def ejercicio2():
    cadena='madrid,sevilla,valencia,córdoba,jaén'
    ciudades=cadena.split(',')
    print(ciudades)
    for ciudad in ciudades:
        print(ciudad)

#ejercicio2()

#Ejercicio 3
def ejercicio3():
    with open('datos.txt','r') as f:
        data=f.read()
        print(data)

ejercicio3()

#ejercicio4