import statistics as mate
if __name__ == '__main__':
    numeros=[10,20,50,80,90,30,40]
#opcion tardada
    conteo=0
    suma=0
    promedio=0

    for n in numeros:
        suma+=n
        conteo+=1

    promedio= suma/conteo

    print(promedio)

    #opcion meio lenta

    suma=0
    for n in numeros:
        suma+=n
    promedio=suma/len(numeros)
    print(promedio)

    #opcion rapida
    promedio==mate.mean(numeros) # mean es un funcion para calcular el promedio de una lista
    print(promedio)