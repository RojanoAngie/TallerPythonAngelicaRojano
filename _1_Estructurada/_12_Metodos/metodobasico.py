import statistics as m
#def suma(a:int,b:int):
 #   print(f"la suma de {a} +{b} es {a+b}")
def suma(a:int,b=None,c=None):
    if b is None:
        print(f"la suma de {a} es {a}")
    else:
        if c is None:
            print(f"la suma de {a} +{b} es {a+b}")
        else:
            print(f"la suma de {a} +{b}  + {c} es {a+b+c}")

def promedioArreglo(lista:list):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p=m.mean(lista)
    print(f"el promedio del {p}")

if __name__ == '__main__':
    suma(10,52,67)
    suma(23,47)
    suma(12,155)
    suma(2)

    lista2=[1,2,3,4,5]
    #similar lista2=lista1

    promedioArreglo(lista2)
    #la lista saldra del metodo alterada, se le llama referencia argumento
    print(lista2)