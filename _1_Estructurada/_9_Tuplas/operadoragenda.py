def extraer (agenda:tuple):
    i:int=0
    while(i<len(agenda)):
        nombre,correo,telenono=agenda[i]
        i+=1
        yield nombre, correo,telenono

if __name__ == '__main__':
    agenda=[]
    agenda.append(("Juan", "Juan@gmail.com", "222343678"))
    agenda.append(("Jonathan", "Jonathan @gmail.com", "222343678"))
    agenda.append(("NIck", "Nick@gmail.com", "222343678"))
    agenda.append(("Rolly", "Rolly@gmail.com", "222343678"))
    agenda.append(("Diana", "Diana@gmail.com", "222343678"))
    agenda.append(("ALma", "akma@gmail.com", "222343678"))
    agenda.append(("Leticia", "Juan@gmail.com", "222343678"))
    agenda.append(("MAriela", "Juan@gmail.com", "222343678"))
    agenda.append(("Monica", "Juan@gmail.com", "222343678"))
    agenda.append(("Juan", "Juan@gmail.com", "222343678"))

    for n,c,t in extraer(agenda):
        print(f"{n}, {c} , {t}")