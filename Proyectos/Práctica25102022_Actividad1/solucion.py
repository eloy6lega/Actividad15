#crear una clase base con los métodos comunes y sus propiedades

class Zoologico:
    @staticmethod #DECLARO EL STATICMETHOD PARA PODER EJECUTARLO BIEN 
    def limpiar_jaula():
        print('Limpiar jaula cuando quieras, estén o no los animales')
    @staticmethod
    def comer():
        print('NO come carne. No es carnívoro')
    @staticmethod
    def visita_publico():
        print('La visita del público comienza de 10:00 a 17:00')

class Leon(Zoologico):
    @staticmethod
    def limpiar_jaula():
        print('Limpiar jaula cuando NO estén los leones')
    @staticmethod
    def comer():
        print('Come carne. Es carnívoro')

class Tigre(Zoologico):
    @staticmethod
    def limpiar_jaula():
        print('Limpiar jaula cuando NO estén los tigres')
    @staticmethod
    def comer():
        print('Come carne. Es carnívoro')

class Perro(Zoologico):
    pass

class Gato(Zoologico):
    pass

class Camello(Zoologico):
    pass

class Delfin(Zoologico):
    @staticmethod
    def visita_publico():
        print('La visita del público comienza de 10:00 a 20:00 - horario ampliado')

class Elefante(Zoologico):
    pass


leon1:Leon=Leon() #tipado fuerte
leon2:Leon=Leon() #interferencia de tipo
camello:Camello=Camello()
gato1:Gato=Gato()
gato2:Gato=Gato()
gato3:Gato=Gato()
delfin1:Delfin=Delfin()
elefante1:Elefante=Elefante()

#muestra como  se limpia la jaula, qué comen y cuándo se puede visitar

arca_de_Noe=[leon1,leon2,camello,gato1,gato2,gato3,delfin1,elefante1] #HAGO UNA LISTA PARA TODOS LOS ANIMALES

for animal in arca_de_Noe: #POLIMORFISMO // RECORRER UNA LISTA
    animal.limpiar_jaula()
    animal.comer()
    animal.visita_publico()