from abc import ABCMeta, abstractstaticmethod
from asyncore import poll3


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_data():
        """ Impelementasi di child class """


class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(seft, name, age):
        if PersonSingleton.__instance != None:
            raise Exception(
                "Single Stone tidak dapat dipakai lebih dari sekali!")
        else:
            seft.name = name
            seft.age = age
            PersonSingleton.__instance = seft

    @staticmethod
    def print_data():
        print(
            f"name : {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")


p = PersonSingleton("Rizal", 21)
print(p)
p.print_data()

p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()

p3 = PersonSingleton.get_instance()
print(p3)
p3.print_data()
