if __name__ == '__main__':

    milista=[1,2,3]
    milista.append(4)
    print(milista)

    #añade los elementos a otra lista

    milista=[1,2,3]
    otraLista=[4,5,6]
    milista.extend(otraLista)
    print(milista)

    #inserta un elemento en una posicion especifica
    milista=[1,2,3]
    milista.insert(1,4)
    print(milista)

    #elimina el primer elemento de la lista en ser encontrado
    milista=[1,2,3,2]
    milista.remove(2)
    print(milista)

    #elimina y devuelve eñ elemento en una posicion
    milista=[1,2,3]
    elemento= milista.pop(1)
    print(milista)
    print(elemento)

    #devuelve el indice de la primera aparicion
    milista=[1,2,3,2]
    indice=milista.index(2)
    print(indice)

    #devuelve el numero de ves qye aparece un elemento
    milista=[1,2,3,2]
    conteo = milista.count(2)
    print(conteo)

    #ordena los slementos de una lista de froma ascendente

    milista=[3,1,4,2]
    milista.sort()
    print(milista)
    #ahora de froma descencentem invierte el orden
    milista.sort(reverse=True)
    print(milista)

    #inierte el orden de los elemetos de la lista
    milista=[4,2,1,3]
    milista.reverse()
    print(milista)

    #elimina todos los elementos de la lista
    milista=[1,2,3]
    milista.clear()
    print(milista)

    #devuelve una copia superficial de la lista
    milista=[1,2,3]
    milista2=milista
    copialista= milista.copy()
    milista.append(4)

    #print(copialista)
    print(milista2)