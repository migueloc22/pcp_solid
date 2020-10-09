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
        return self.cnn
    def  setDatos(self,cnn):
        self.cnn=cnn
class APIService(Conexion):
    def  getDatos(self):
        return self.cnn
    def  setDatos(self,cnn):
        self.cnn=cnn
api = APIService()
api.setDatos('esta la coonecion de la api')
print(api.getDatos())
db = DatabaseService()
db.setDatos('esta la coonecion de la db')
print(db.getDatos())