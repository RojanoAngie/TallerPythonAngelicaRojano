if __name__ == '__main__':
    n=int(input("Cuantos nombres quieres ingresar"))

    largo=[0,0,0,0,0,0,0,0,0,0]
    extras:int=1
    for i in range(n):
        nombre=str(input("ingrese un nombre"))
        tam=len(nombre)
        match tam:
            case 1:largo[0]+=1
            case 2:largo[1]+=1
            case 3:largo[2]+=1
            case 4:largo[3]+=1
            case 5:largo[4]+=1
            case 6:largo[5]+=1
            case 7:largo[6]+=1
            case 8:largo[7]+=1
            case 9:largo[8]+=1
            case 10:largo[9]+=1
            case _: extras+=1

    i:int=1
    for n in largo:
        print(f"el total de nombres con {i} letras:{n}")
        i+=1
    print(f" el total de nombres con mas de 10 letras: {extras}")