if __name__ == '__main__':
    agenda={}

    agenda["GOAT800717"]=("Tomas Gonzales", "csctomasgonzales@gmail.com", "2223848670")
    agenda["GOAT8007179"]=("LUIS Gonzales", "csctomasgonzales@gmail.com", "2223848670")
    agenda["GOAT800718"]=("Fabioa Gonzales", "csctomasgonzales@gmail.com", "2223848670")
    agenda["GOAT800710"]=("Fernand Gonzales", "csctomasgonzales@gmail.com", "2223848670")

    nombre, correo, numero=agenda[("GOAT8007179")]

    print(f"los datos del ref som: nombre: {nombre}, correo: {correo} y numero:{numero}")