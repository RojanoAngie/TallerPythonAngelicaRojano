class ListaDatos:

    def __init__(self, matricula: str, estudiante: str, asignatura: str):
        self.matricula = matricula
        self.estudiante = estudiante
        self.asignatura = asignatura

class ControlEscolar:
    def __init__(self):
        self.lista=[]

    def addEstudiantw(self, matricula, estudiante, asignatura):
        self.lista.append(ListaDatos(matricula, estudiante, asignatura))

    def show (self):
        for obj in self.lista:
            print(f"Matricula: {obj.matricula}")
            print(f"Nombre: {obj.estudiante}")
            print(f"Asignatura: {obj.asignatura}")
            print("_______________________")


if __name__ == '__main__':
    escolar=ControlEscolar()
    escolar.addEstudiantw("123545", "Paloa SUarez", "Quimica")
    escolar.addEstudiantw("123545", "Paloa SUarez", "Quimica")
    escolar.addEstudiantw("123545", "Paloa SUarez", "Quimica")
    escolar.addEstudiantw("123545", "Paloa SUarez", "Quimica")
    escolar.addEstudiantw("123545", "Paloa SUarez", "Quimica")

    escolar.show()
