# from abc import ABCMeta, abstractmethod
from abc import ABC,abstractmethod

class Coche(ABC):
    @abstractmethod
    def  precioMedioCoche(self):
        pass

class Renault(Coche):
    def  precioMedioCoche(self):
        return 18000
class Audi (Coche):
    def  precioMedioCoche(self):
        return 25000
class Mercedes (Coche):
    def  precioMedioCoche(self):
        return 27000

def imprimirPrecioMedioCoche(coches):
    for coche in coches:
        print(coche.precioMedioCoche())

if __name__ == "__main__":
    Coche=[Renault(),
            Audi(),
            Mercedes()
        ]
    # print(Coche[0].precioMedioCoche())
    imprimirPrecioMedioCoche(Coche)

