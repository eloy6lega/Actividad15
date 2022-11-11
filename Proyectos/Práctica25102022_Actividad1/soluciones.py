#diseña una función sin argumentos
#pide las unidades y el precio : calculas el subtotal
#el iva es 21%
#muestra por consola el subtotal y la cuota de iva

from datetime import date, datetime
from re import sub
from tkinter import dialog

def calcular():
    try:
        unidades=int(input('Introduce las unidades: '))
        precios=float(input('Introduce las precio: '))
        iva=0.21
        subtotal=unidades*precios
        cuota=subtotal*iva
        print(f'El subtotal es {subtotal}€')
        print(f'la cuota de iva es {cuota}€')
    except:
        print('Revisa los valores introducidos...')

calcular()

#pides una ciudad
#muestras la ciudad en MAYÚSCULAS y las aes son ies
#si es madrid, no hay ningún cambio. saldrá como se escribe 
#dentro de una función

def cambiarCiudad():
    ciudad=input('Dime una ciudad: ')
    if ciudad.lower()!='madrid':
        print(ciudad.lower().replace('a', 'i').upper()) #MIDRID
    else:
        print(ciudad.upper())

cambiarCiudad() #invoco la función

#pides un email
#si no tiene @ muestra mensaje indicando email no válido
#si el email es correcto, tiene @, te dice que email guardado
#todo en una función (sin argumentos)

def pideCorreo():
    email=input('Dime tu email: ')
    if "@" in email:
        print('Correo guardado')
    else:
        print('Correo no válido')

pideCorreo() #invoco


#pide la fecha de alta
#respecto al día de hoy, muestra los días que llevas de alta

alta=input('Introduce la fecha de alta (yyyy-mm-dd): ')
altaFecha=datetime.strptime(alta,'%Y-%m-%d')
hoy=datetime.now()
dias=hoy-altaFecha
print(dias)