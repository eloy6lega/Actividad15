#te vas a matricular en varias asignaturas
#por consola te piden que introduzcas el nombre de la asignatura
#te siguen preguntando mientras no le digas q
#al salirte, te muestra las asignaturas en las que te has matriculado
#no puede salir una asignatura repetida


print("Matrícula de alumno")
asignaturas={''} #declaro el Set
while True:
    asignatura=input("dime qué asignatura quieres ")
    if asignatura=='q':
        break
    asignaturas.add(asignatura)
asignaturas.remove('')   
print(asignaturas)
for a in asignaturas:
    print(a)