pregunta = input("¿Qué profesión querías ser de pequeño? ")

match pregunta:
    case "bombero":
        print("Típico niño con padre gymrat")

    case "policía":
        print("El clásico de clase. Probablemente te gustaba una chica distinta cada año")

    case "veterinario":
        print("Te gustan los animales, me gusta...")
    
    case "vagabuendo":
        print("Sinceramente, EL PUTO AMO. Tendrás éxito en todooo!!!")

    case _:
        print("Igual estás destinado a no tener futuro...quien sabe.")