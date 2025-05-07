if __name__ == '__main__':
    numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19, 20]

    listaPares=list(filter(lambda x: x%2==0, numeros)) #FILTER ES UN FOR QUE CONTIENE UN IF, SIEMPRE DEVUELVE UNA LISTA
    listaImpares=list(filter(lambda x: x%2==1, numeros))

    print(f"la lista de numeos pares: {listaPares}")
    print(f"la lista de numeos impares: {listaImpares}")

    #PERO SI antes queremos elevar al cuadrado los impares:
    #                            map necesita una lista, y filter regresa la lista
    listaImparesConPotencia=list(map(lambda z: z**2, filter(lambda t: t%2==1, numeros)))

    print(f"la lista de impares elevado al cuadrado es {listaImparesConPotencia}")