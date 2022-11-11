from ast import USub


nombre='luis' #declaración de variable
print(nombre)
numero1='15'
numero2=5.95 #si se ponen aquí las comillas da error porque es un tipo float y el otro int
total=int(numero1)*numero2 #cast, parsing
print(total)
print(8**2) #64
print(7/3) #división
print(7%3) #módulo (resto de la división)
print(7//3) #te da el número entero de la división SIN aproximar

ciudad=input('dime una ciudad ') #me preguntará una ciudad, y yo le digo una, según la que le diga me dirá lo que hemos programado
#print(len(ciudad)) y me dirá las letras de la ciudad
if ciudad=='sevilla': #si la ciudad es sevilla...
    print('estamos de feria') #dirá estamos de feria
elif ciudad=='madrid': #si la ciudad es madird...
    print('bienvenidos') #dirá bienvenidos
else: #si no es ni una ni otra
    print('que aburrimiento') #dirá que aburrimiento

datos=['malaga', 15, 8.95, True, 'laura', 147] #varios tipos de datos en la misma línea
for dato in datos : #con este comando decimos, para dato en datos...
    print(dato, len(str(dato))) #nos nombrará cada dato de datos y ademas al meter la función len nos dará el numero de caracteres de cada palabra/número
print(len(datos)) #te dirá la cantidad de valores en datos 
print(datos[5]) #el corchete te dice que elemento del arraid (datos) quieres que te muestre (dará error con 6 porque empieza a contar desde el 0 para este comando, con lo cual funcionará con 5(147))
print(datos[-1]) #nos dará el último dato de datos (147)

#tarea
usuario='admin'
contraseña='123'
usuario=input('Introduzca el ususario con el que desea entrar: ')
contraseña=input('Introduce la contraseña: ')
if usuario=='admin' and contraseña=='123':
    print('Bienvenido al sistema Señor Stark')
else:
    print('error de inicio de sesión, has sido expulsado del sistema')
print('Fin de validación')

#Tarea2
#por pantalla te pide las unidades, las introduces
#si las unidades son mayor que 10, su precio es 9.95
#y muestras el total.
#si son menor o igual a 10, el precio es 14.95
#cuidado con casting de tipos de datos

unidades=int(input('dime las unidades '))
if unidades>10:
    print(unidades*9.95)
else:
    print(unidades*14.95)