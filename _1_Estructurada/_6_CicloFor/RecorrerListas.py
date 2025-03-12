if __name__ == '__main__':
    lista=[1,2,3,"lunes",4,5,6,7,8,9,10,11,12,13,14,15,16] #lista mutable
    #agrega diferentes tipos de datos, tipo de dato object

    for elemento in lista:
        print(elemento)


    lista.append(200)
    lista.append("Jonathan")
    lista.append(28.9680)
    lista.append(True)
    lista.append(87.988)

    lista2=[1200,58,"Nick"]
    lista.append(lista2)

    for elemento in lista:
        print(elemento)

    nombre:str
    nombre="Luis"

    nombre += "Gutierrez"
    print(nombre)
    nombre.join("Gutierrez")

    print(nombre)

    lista3= ["Federico", "pablo", "Karla"]

    cadena:str=" - ".join(lista3) #se utiliza la funcion join para incluir los elemnetos en un caracter
    print(cadena)

    #split se utiliza para separar los elementos
    separado=cadena.split()
    for dato in separado:
        print(dato)