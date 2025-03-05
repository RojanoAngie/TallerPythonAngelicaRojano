if __name__ == '__main__':
    a=int(input("ingrese un numero:"))
    b=int(input("ingrese un numero:"))
    c=int(input("ingrese un numero:"))

    if a>b:
        if a>c:
            print(f"EL mayor es {a}")
        else:
            print(f"EL mayor es {c}")#alt+shift+flechita para mover la linea
    else:
        if b>c:
            print(f"EL mayor es {b}")#alt+shift+flechita para mover la linea
        else:
            print(f"EL mayor es {c}")#alt+shift+flechita para mover la linea

