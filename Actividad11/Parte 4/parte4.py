
def archivo_inpu():
    ejemplo = open("5preguntasEloy.txt", 'w')
    x='¿Nombre y Apellidos?'
    b='¿Valor de las joyas que tienes en casa?'
    c='¿Donde guardas las joyas en casa?'
    g='¿A qué hora no estás en casa?'
    j='¿Que días no estáis en casa?'
    ejemplo.write(f"{x}\n")
    ejemplo.write(f"{b}\n")
    ejemplo.write(f"{c}\n")
    ejemplo.write(f"{g}\n")
    ejemplo.write(f"{j}")
    ejemplo.close()

    ejemplo=open('5preguntasEloy.txt','r')
    print(ejemplo.read())
archivo_inpu()