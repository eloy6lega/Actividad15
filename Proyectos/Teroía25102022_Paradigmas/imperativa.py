#poo, estructura, procedimental

#Problema. Aplicar un descuento si las unidades son +10
#serie de pasos que implementan el programa que resuelve el algoritmo
#programación secuencial
unidades=20
respuesta=""
if unidades>=10:
    respuesta="Se aplica descuento"
else:
    respuesta="No se aplica descuento"

print(respuesta)


#el cliente ha comprado 1000000 tipos diferentes de productos
#bucle para todos los elementos y comprobar si se aplica o no descuento

def tieneDescuento(unidades):
    respuesta="" #mutabilidad variable
    if unidades>=10: #estructura cíclica
        respuesta="Se aplica descuento"
    else:
        respuesta="No se aplica descuento"

    print(respuesta)

productos_unidades=[15,8,9,24,36]
for producto in productos_unidades:
    tieneDescuento(producto)