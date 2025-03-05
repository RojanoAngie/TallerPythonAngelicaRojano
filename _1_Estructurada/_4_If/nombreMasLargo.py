if __name__ == '__main__':
    n1=str(input("ingrese un nombre:"))
    n2=str(input("ingrese otro nombre:"))

    l1=len(n1)
    l2=len(n2)

    if l1>l2:
        print(f"el nombre mas largo es: {n1}")
    else:
        if l1<l2:
            print(f"el nombre mas largo {n2}")
        else:
            print(f"los nombres {n1} y {n2} son igual de largos")


