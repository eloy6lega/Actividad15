Algoritmo array_aletorios
	Dimension A[10]
    
    // recorre los 10 elementos y va asignandoles enteros aleatorios
    para cada elemento de A Hacer
        // elemento toma el contenido de cada posicion del arreglo
        // y si se modifica elemento se modifica el arreglo
        elemento <- azar(100)
    FinPara
    
    Escribir "Los elementos del arreglo son:"
    // recorre los 10 elementos utilizando subindices y los muestra en pantalla
    para i desde 1 hasta 10 Hacer
        escribir "Posici�n " i ": " A[i]
    FinPara
    
    Escribir "" // deja una linea en blanco
    
    Escribir "En orden inverso:"
    // recorre los 10 elementos en orden inverso y los muestra en una misma linea
    para i desde 10 hasta 1 Hacer
        escribir sin bajar A[i] " "
    FinPara
FinAlgoritmo
