### classes ###

class Person:
    pass

print (Person)

class MyPerson:
    def __init__(self, name, surname, alias ="sin alias"): #constructor de clases
        self.full_name = f"{name} {surname} {alias}"

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = MyPerson("rodolfo", "jesusrlv")
print(my_person.full_name)
my_person.walk()

my_other_person = MyPerson("Rodolfo","rojo","jesusrlv")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "JesusR leaños"
print(my_other_person.full_name)
