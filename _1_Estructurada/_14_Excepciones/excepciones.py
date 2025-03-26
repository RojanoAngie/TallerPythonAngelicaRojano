if __name__ == '__main__':
    try:

        numero=int(input("introduce un numero"))
        resultado= 10/numero

    except ValueError:
        #si se introduce un valor no numerico
        print("Error, debes introducir un numero entero")
    except ZeroDivisionError:
        #manejo de la excepcion si se intenta dividir por cero
        print("Error, no se puede dividirentre cero")

    else:
        #seejcuta si no hubo excepciiones
        print("el resultado es: ", resultado)

    finally:
        print("fin delprograma")