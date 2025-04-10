class ListaDatos:

    def __init__(self, matricula:str, estudiante:str, asignatura:str):
        self.matricula=matricula
        self.estudiante=estudiante
        self.asignatura=asignatura


if __name__ == '__main__':
    lista=[]
    lista.append(ListaDatos("1258658", "Juan CArlos", "ESpañol"))
    lista.append(ListaDatos("1257899", "Cecilia Rocha", "Matematicas"))
    lista.append(ListaDatos("1212345", "Federico Cortes", "Quimica"))
    lista.append(ListaDatos("1234556", "Paola Flores", "Fisica"))

    for obj in lista:
        print(f"Matricula: {obj.matricula}")
        print(f"Nombre: {obj.estudiante}")
        print(f"Asignatura: {obj.asignatura}")
        print("_______________________")
