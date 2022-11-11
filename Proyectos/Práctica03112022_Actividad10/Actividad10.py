
from datetime import datetime

print('_____________________________________________________________________________________________________________________________________________________________________________')

print('¡¡¡BIENVENIDO AL SISTEMA!!!')
print(' ')
usuario = input(f'Introduzca su nombre para registrarse en el sistema: ')
print(f'¡¡¡BIENVENIDO AL SISTEMA, {usuario}!!!')

fecha_rev = input('Introduzca una fecha para ver su agenda del formato dd-mm-yyyy: ')

print(f'Usted ha introducido la siguiente fecha, {fecha_rev}...')

fecha_rev_for=datetime.strptime(fecha_rev,'%d-%m-%Y')
finsemana=fecha_rev_for.weekday()

print('revisando...')
print('.')
print('.')
print('.')

if finsemana < 5 and (fecha_rev_for.day in (5,9,14,12)):
    print(f'En su agenda tiene apuntado NATACIÓN, {usuario}')
if finsemana < 5 and (fecha_rev_for.day in (14,19,28)):
    print(f'En su agenda tiene marcado INGLÉS, {usuario}')
elif finsemana== 5:
    print(f'En su agenda tiene partido de baloncesto, {usuario}')
else:
    print(f'Agenda vacía mi señor')


print('APAGANDO EL SISTEMA')
print('_____________________________________________________________________________________________________________________________________________________________________________')


