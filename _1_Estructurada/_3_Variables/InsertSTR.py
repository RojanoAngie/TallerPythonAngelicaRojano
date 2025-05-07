if __name__ == '__main__':
    palabra:str="%s"
    lista:list=["nombre", "apellido_patermo", "nombre_usuario", "edad", "correo electronico", "contrasenia"]
    lista2: list=[]
    print(palabra)
    #palabra = palabra*5

    t= len(lista)
    print(t)
   # palabra= palabra*len(lista)

    print(palabra)
    campos=", ". join(lista) #resulta asi: "nombre", "apellido_patermo", "nombre_usuario", "edad", "correo electronico", "contrasenia"
    print(campos)


    for i in range(t):
        lista2.append(palabra)

    valores=", ".join(lista2)
    querySQL=f"INSERT INTO tabla ({campos}) values ({valores})"
    print(querySQL)