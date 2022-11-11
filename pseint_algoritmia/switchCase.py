print('Elige una opción de las siguientes')
print('1 - Programación')
print('2 - Base de datos')
print('3 - Entornos de desarrollo')
print('4 - Sistemas informáticos')
opcion=input('dime el número de la opción elegida')
match opcion:
    case '1':
        print('vemnos python, php y java')
    case '2':
        print('vemos mysql, oracle, posgres y mongodb')
    case '3':
        print("aquí vemos eclipse y netbeans")
    case '4':
        print("aquí windows y linux")
    case _:
        print("esta opción no es válida")