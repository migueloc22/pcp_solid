class Coche():

    marca = ''
    #construtor
    def __init__(self, marca):
         self.marca= marca
    def getMarcaCoche(self):
        return self.marca

class CocheDB():
    def guardarCocheDB(self, coche):
        print ('El coche guardado de la marca : '+coche.getMarcaCoche())
    def eliminarCocheDB(self,coche):
        print ('El coche aliminado de la marca : '+coche.getMarcaCoche())
    pass
coche =  Coche('mercedes')
cocheDB = CocheDB()
cocheDB.eliminarCocheDB(coche)
    