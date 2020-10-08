from abc import ABC,abstractmethod
class Conexion  (ABC):
    @abstractmethod
    def  getDatos(self):
        pass
    @abstractmethod
    def  setDatos(self):
        pass
class DatabaseService(Conexion):
    def  getDatos(self):
            pass
    def  setDatos(self):
        pass
class APIService(Conexion):
    def  getDatos(self):
            pass
    def  setDatos(self):
        pass