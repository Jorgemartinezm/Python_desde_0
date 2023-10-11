### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name # Propiedad privada
        self.__surname = surname
        
    def get_name(self):
        self.__name
        
    def walk(self):
        print(f"{self.full_name} Está caminando")

my_person = Person("Jorge", "Martínez")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Jorge", "Martínez", "R3dlight")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El Loco de los Perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)