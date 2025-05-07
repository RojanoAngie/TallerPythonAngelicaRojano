if __name__ == '__main__':
    lambdaSuma= lambda x,y: x+y

    valor1=int(input("dame un numero"))
    valor2=int(input("dame un numero"))

    suma= lambdaSuma (valor1, valor2)
    print(f"{valor1} + {valor2} = {suma}")