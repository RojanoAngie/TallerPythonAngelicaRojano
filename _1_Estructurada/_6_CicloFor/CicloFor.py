import sys
if __name__ == '__main__':

    for i in range(10):
        print(f"{i}")

    print("---------")
#(inicio, fin)
    for i in range(6,12):
        print (f"{i}")

    print("---------")
#(inicio, fin,incremento)
    for i in range(6,12,3):
        print(f"{i}", end=" ") #end=" " anula saltos de linea

    print("---------")

    for i in range(12,6,-3):
        print(f"{i}")


sys.stdout.write("Texto sin salto de linea") #no hace salto de linea