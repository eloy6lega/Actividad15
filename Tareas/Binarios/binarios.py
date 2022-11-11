#conversión de números
#pides un número decimal: 192
#muestras el número binario

def pasarBinario():
    decimal=int(input('Dime un número ENTERO y POSITIVO para convertir a lenguaje binario: '))
    binario=bin(decimal)
    print(binario)

pasarBinario()
