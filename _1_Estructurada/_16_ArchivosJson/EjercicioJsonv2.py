import json
import sys
def miiterador():
    try:
        informacion= open("informacion.json", "r", encoding="utf-8")
        datos= json.load(informacion)

        for persona in informacion["personas"]:
            yield ( persona["id"], persona["nombre"], persona["edad"], persona["RFC"])

    except FileNotFoundError:
        print(RED, "Error, el archivo no existe")
    except json.decoder.JSONDecodeError:
        print(RED, "Error, el archivo no contiene un JSON ")
    except Exception as e:
        print(GREEN,"Pues no se que ocurrio", e)
    else:
        informacion.close()
        print(RESET, "Archivo cerrado")


if __name__ == '__main__':
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    i=1
    for id, nombre, edad, RFC in miiterador():
        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(GREEN)
            case 3:
                sys.stdout.write(BLUE)
            case 4:
                sys.stdout.write(YELLOW)
            case 5:
                sys.stdout.write(RED)
            case 6:
                sys.stdout.write(GREEN)
            case 7:
                sys.stdout.write(BLUE)
            case 8:
                sys.stdout.write(YELLOW)
            case _:
                sys.stdout.write(RESET)

        print(id,nombre,edad,RFC)

        if edad<18:
            print(f"{nombre} es menor de edad")
        else:
            print(f"{nombre} es mayor de edad")
        print("------------------")
        i+=1