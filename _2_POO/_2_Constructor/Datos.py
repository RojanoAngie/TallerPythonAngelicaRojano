class Datos:

    def __init__(self, nombre,correo,whatsapp):
        self.nombre=nombre
        self.correo=correo
        self.whatsapp=whatsapp

    def setNombre(self,nombre):
        self.nombre=nombre

if __name__ == '__main__':
    datos=Datos("Tomas","csctomasgonzales@gmail.com", "246178192")

    print(datos)
    datos.setNombre("Gabriel")
    print(datos)
    datos.nombre("Jonathan")
    print(datos)

