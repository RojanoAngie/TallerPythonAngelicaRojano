def suma (a:int,b:int)-> int:
    return a+b
def arreglo(lista:[])->int:
    return sum(lista)


if __name__ == '__main__':
    print(f"la suma es {suma(15,22)}")
    lista=[1,2,3,4,5]
    print(f"la suma del arreglo es {arreglo(lista)}")