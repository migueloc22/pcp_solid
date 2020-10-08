from abc import ABC,abstractmethod

class Coche(ABC):
    @abstractmethod
    def  numAsientos(self):
        pass
class Renault(Coche):
    def  numAsientos(self):
        return 5
class Audi (Coche):
    def  numAsientos(self):
        return 6
class Mercedes (Coche):
    def  numAsientos(self):
        return 2

def imprimirNumAsientos(coches):
    for coche in coches:
        print(coche.numAsientos())
Coche=[Renault(),
        Audi(),
        Mercedes()
    ]
imprimirNumAsientos(Coche)