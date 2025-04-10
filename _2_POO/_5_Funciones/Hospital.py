class Hospital:
    def __init__(self): #para vertir en privadi agregar __ :      self.__NombrePaciente:str=""

        self.__NombrePaciente:str=""
        self.__nss:int=1258
        self.__enfermedad:str=""

    def getNombrePaciente(self)->str: #se puede usar el mismo __ paara aqui
        return self.__NombrePaciente

    def getNss(self)->int:
        return self.__nss

#decorador arriba de los getters se colca funciones
    @property #esto convierte el metodo de una propiedad en solo lectura
    def getEnfermedad(self)->str:
        return self.__enfermedad

    def setNombrePaciente(self, nombre:str):
        self.NombrePaciente=nombre

    def setNss(self, nss):
        self.nss=nss

    def setEnfermedad(self, enfermedad:str):
        self.enfermedad=enfermedad

if __name__ == '__main__':
    hospital=Hospital()

    hospital.setNombrePaciente("Juan")

    print(hospital)
    print(hospital.getNombrePaciente) #se puede usar sin paremntesis por el properties