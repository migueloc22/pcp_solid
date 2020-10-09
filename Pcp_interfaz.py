from abc import ABC,abstractmethod
class IAveVoladora (ABC):
    @abstractmethod
    def  volar(self):
        pass
class IAve(ABC):
    @abstractmethod
    def  comer(self):
        pass
class IAveNadadora (ABC):
    @abstractmethod
    def  nadadora(self):
        pass
class Loro (IAve,IAveVoladora):
    def volar(self):
        return 'Loro vuela.'
    def comer(self):
        return 'Loro come.'
class Tucan  (IAve,IAveVoladora):
    def volar(self):
        return 'Tucan vuela.'
    def comer(self):
        return 'Tucan come.'
class Pinguino (IAve,IAveNadadora):
    def comer(self):
        return 'pinguino come.'
    def nadadora(self):
        return 'pinguino nada.'

aves=[
    Loro(),
    Tucan(),
    Pinguino()
]
def imprimirAve(aves):
    for ave in aves:
        print(ave.comer())
imprimirAve(aves)