#array
import random

num=[]
for n in range(10):
   num.append(random.randrange(1,100,1))

print(num)
print('Los elementos de la lista son: ')

for i in num:
    print(f'En la posicion {num.index(i)} el número es: {i}')

print(' ')
num.reverse()

for i in num:
    print(i,end=' ')
