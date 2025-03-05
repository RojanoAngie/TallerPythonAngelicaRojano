if __name__ == '__main__':

    x=int(input("ingresa un numero: "))
    y=int(input("ingresa la potencia: "))

    i:int=0;
    pot:int=1;

    while i<y:
        pot=pot*x
        i+=1
        #ta,bien se puede poner asi:  pot=pot*x; i+=1
    print(f'El resultado de {x} ^ {y} = {pot}')
