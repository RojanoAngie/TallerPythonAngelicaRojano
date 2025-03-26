def calculararea(rectangulo:tuple[int,int])-> int:
    #extrae respectivamente los valores de la tupla
    largo, ancho= rectangulo

    return largo*ancho

def cuadrado(rectangulo:tuple[int,int])->int:
    largo,ancho=rectangulo
    largo=largo*largo
    ancho=ancho+ancho
    return (largo,ancho)

if __name__ == '__main__':
    dimensiones=(10,5)

    area=calculararea(dimensiones)
    print(f"el area del rectangulo es: {area}m cuadrados")

    largo,ancho=cuadrado((5,3))

    print(f"el largo es: {largo} y amcho {ancho}")