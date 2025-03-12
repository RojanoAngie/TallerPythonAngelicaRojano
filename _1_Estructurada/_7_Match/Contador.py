if __name__ == '__main__':
    lista=[1,5,6,4,7,89,4,7,1,67,56,8,9,1,4,10,1,5,6,3]
    totales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    adoptados: int = 0

    for elemento in lista:
        match elemento:
            case 1:
                if elemento == 1:
                    totales[0]+= 1
            case 2:
                if elemento == 2:
                    totales[1]+= 1
            case 3:
                if elemento == 3:
                    totales[2]+= 1
            case 4:
                if elemento == 4:
                    totales[3]+= 1
            case 5:
                if elemento == 5:
                    totales[4]+= 1
            case 6:
                if elemento == 6:
                    totales[5]+= 1
            case 7:
                if elemento == 7:
                    totales[6]+= 1
            case 8:
                if elemento == 8:
                    totales[7]+= 1
            case 9:
                if elemento == 9:
                    totales[8]+= 1
            case 10:
                if elemento == 10:
                    totales[9]+=1
            case _: adoptados+= 1
    i:int=1
    for n in totales:
        print(f"{i}.-{n}")
        i+=1
    print(f"adoptados = {adoptados} ")

