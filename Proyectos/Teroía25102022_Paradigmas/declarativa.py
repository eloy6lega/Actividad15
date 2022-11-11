#funcional, reactiva, procedimental

#Problema. Aplicar un descuento si las unidades son +10

#productos_unidades=[15,8,24,36]
#def tienedescuento(unidades):
#    if unidades >= 10: #estructura ciclica
#        respuesta="Se aplica descuento"
#    else:
#        respuesta="No se aplica descuento"
#    print(respuesta)

#descuento = filter(lambda n: n>=10, productos_unidades)
#print(list(descuento))

productos_unidades=[15,8,24,36]
descuento = filter(lambda n: n>=10, productos_unidades)
print(list(descuento))