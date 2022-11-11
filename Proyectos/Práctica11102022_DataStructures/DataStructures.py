from statistics import mean

#ejercicio 1
#Crea una lista con 6 ciudades
#Muestra las ciudades por consola
#En mayúsculas y al lado el número de letras que tiene

#si vas a poner ciudades repetidas mejor usar un set
ciudades={'madrid','sevilla','valencia','jaén','córdoba','sevilla'}
print(ciudades) #comprobación. Para mostrar las ciudades es mejor recorrerlas con un for :
for ciudad in ciudades:
    print(f'Ciudad: {ciudad.upper()} -- {len(ciudad)}')

#ejercicio 2
#Crea una colección con 5 marcas de coche
#Muestra el listado de ordenado en orden desdendente

#Para ordenar tiene que ser list
coches=['audi','mercedes','bmw','toyota','tesla']
#Con estos dos comandos primero ponemos que salgan los coches en el orden alfabético y con el segundo al revés (en ves de a-z, de z-a)
coches.sort()
coches.reverse()
for coche in coches:
    print(coche)

#ejercicio 3
#Crea una colección con 5 clientes y su facturación anual en euros.
#Muestra el total de facturación y la facturación media.
clientes={'indra':147.95,'bbva':159.78,'minsait':148.54,'santander':963.54,'once':147.45}
total=0 #acumulador
for k,v in clientes.items():
    total=total+v
print(f'El total es {total}')
print(f'La media de facturación es: {total/len(clientes)}')

#ejercicio 4
#Por consola te pide un número hasta que pulses 0.
#Muestra la suma total de estos números.
total=0 #acumulador
numero=int(input('Dime un número para sumarlo hasta que pulses 0: '))

while numero!=0:
    total=total+numero
    numero=int(input('Dime otro número: '))
print(f'La suma total es {total}')

#ejercicio 5
#En una colección introduce los precios de 5 artículos.
#No necesitamos los nombres de los artículos. (Puedes prescindir de diccionario)
#Muestra el precio promedio. Si es superior a 5, indica que debemos bajar el precio un 5%

articulos={'camisa':19.99,'sombrero':9.99,'pantalon':14.99,'abrigo':20.99,'chaqueta':59.99}
#Método 1
total=0
for k,v in articulos.items():
    #total=total+v
    total+=v
print(f'La media de precios es: {total/len(articulos)}')

if(total/len(articulos))>5:
    print('Debemos bajar los precios un 5%')

#Método 2 - programación funcional. funciones que simplifican condicional como bucles
print(sum(articulos.values()))
print(mean(articulos.values()))

if(total/len(articulos))>5:
    print('Debemos bajar los precios un 5%')