if __name__ == '__main__':
    m=int(input("ingrese el numero que quiere multilpicar"))
    n=int(input("ingrese el numero por el que quiere multplicar"))

    i:int=0 #vuelta que da la iteracion,
    m1:int=0

    while i<n: #segun aqui
        m1=m1+m
        i+=1

        print(f'el resultado de {m} x {i} es: {m1}') #aqui vemos comoi es las veces que se repite el ciclo

    print(f'el resultado de {m} x {n} es: {m1}')
