if __name__ == '__main__':
    diccionario={
        ("id","int"):'2',
        'nombre':'juan',
        'apellido': 'Gitierrez'
    }

    diccionario[("ana",25)]="Esrudiante"
    diccionario[("luis",30)]="Ingeniero"
    diccionario[("ana",25)]="abogad0"

    ocupacion_ana=diccionario[("ana",25)]
    ocupacion_luis=diccionario [("luis",30)]

    print(f"Ana es: {ocupacion_ana}")
    print(f"luIS es: {ocupacion_luis}")
