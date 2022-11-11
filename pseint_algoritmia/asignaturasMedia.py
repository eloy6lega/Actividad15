asignaturas=int(input('cuántas asignaturas tienes '))
totalNota=0 #acumulador
for i in range(asignaturas):
    nota=int(input(f'dime la nota de la la asignatura {i} '))
    #totalNota=totalNota+nota
    totalNota+=nota
notaMedia=totalNota/asignaturas
print(f'tu nota media es {notaMedia}')