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
        pass
    def comer(self):
        pass
class Tucan  (IAve,IAveVoladora):
    def volar(self):
        pass
    def comer(self):
        pass
class Pinguino (IAve,IAveVoladora):
    def comer(self):
        pass
    def nadar(self):
        pass

