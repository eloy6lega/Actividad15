from random import random


from random import randint
listado=[] #Dimension A[10] - Python el listado es dinámico
for numero in range(10): #10 posiciones las que almacenas
    listado.append(randint(1,100))
print(listado) 
#también se puede hacer un bucle para pintarlo
for i in listado:
    print(i)
#fin del bucle
listado.reverse() #ordenar en modo descendente
print(listado)
