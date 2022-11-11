def calcular(x,y): #definir una función
    return x+y

#sobrecarga de métodos, overload
def calcular(x,y,z):
    return x+y+z

#suma=calcular(5,7) #invocar una función #me estorba para los pares
#calcular(8,8,7) #pongo el hastag aquí y abajo para que no me estorbe en el código de los números pares
#print(suma)

#tienes una función que pide como parámetro el producto
#si metes camisa le muestras un mensaje indicando que no hay stock
#cualquier otro producto, le dices que todavía hay existencias

def comprobarStock(producto):
    if producto=='camisa':
        print('Lo sentimos, no tenemos en stock')
    else:
        print('aún quedan existencias')

#comprobarStock('camiseta') #invocar la función #pongo el '#' aquí para que no me estorbe ne el código de abajo

#crear una función sin arguentos
#te pregunta por un número
#mestras desde el 1 los números pares hasta ese número
#invoca la función y prueba

def mostrarPares():
    try:
        limite=int(input('Dime un número hasta el cual te diré los pares: '))
        for n in range(2,limite,2): #Empezará desde el dos hasta el límite contando de dos en dos
            if n==14:
                break #sale de todo el bucle cuando llega a 14 (nunca llegará al 16)
                #continue #sale de este iterator pero NO del bucle completo
            print(f'-{n} ')
        print('fin de números pares')
    except:
        print('Error por algo. No lo sé...')

#el try-except de PYTHON es el try-catch de CUALQUIER OTRO

#invocar
mostrarPares()

#crear una función con un array que contiene 5 ciudades
#le pasas como parámetro la ciudad que quieres mostrar
#la pintas en consola

def mostrarCiudades(pos): #definir
    ciudades=['albacete','oropesa del mar','madrid','orcasitas','palencia']
    print(f'La ciudad elegida es: {ciudades[pos]}')

mostrarCiudades(1) #invocar. Cuidado porque empieza a contar desde el 0, 0=albacete; 1=oropesa del mar; 2=madrid...
